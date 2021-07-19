import paramiko
import time
import sys
from scp import SCPClient
from txt_rw import write_to_log



class RbUpdater:
    # DebugLevel = 3: Todos os alertas
    # DebugLevel = 2: Importantes e comandos
    # DebugLevel = 1: Apenas importantes
    # DebugLevel = 0: Nenhum alerta

    def __init__(self, host, port, user, pwd, debug):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.DebugLevel = debug

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            write_to_log('Conectando em {0}@{1}:{2}'.format(self.user, self.host, self.port))
            self.ssh.connect(self.host, self.port, self.user, self.pwd, banner_timeout=200)
            return self
        except paramiko.ssh_exception.AuthenticationException:
            write_to_log('Error: ssh_exception.AuthenticationException')
            return 'password'
        except paramiko.ssh_exception.NoValidConnectionsError:
            write_to_log('Error: ssh_exception.NoValidConnectionsError')
            return 'connection error'
        except TimeoutError:
            write_to_log('Error: connection timeout')
            return 'connection error'
        except paramiko.ssh_exception.SSHException:
            write_to_log('SSHException: Error reading SSH protocol banner')
            return 'connection error'

    def exec_command(self, cmd, output=False):
        shell_output = []

        if type(cmd) == list:
            for c in cmd:
                write_to_log('ssh.exec_command: ' + c)
                stdin, stdout, stderr = self.ssh.exec_command(c)

                if output:
                    for line in stdout:
                        write_to_log('ssh.output: ' + line.strip('\n'))
                        print(line.strip('\n'))
                else:
                    for line in stdout:
                        write_to_log('ssh.output: ' + line.strip('\n'))
                        shell_output.append(line.strip('\n'))
        else:
            write_to_log('ssh.exec_command: ' + cmd)
            stdin, stdout, stderr = self.ssh.exec_command(cmd)

            if output:
                for line in stdout:
                    write_to_log('ssh.output: ' + line.strip('\n'))
                    print(line.strip('\n'))
            else:
                for line in stdout:
                    write_to_log('ssh.output: ' + line.strip('\n'))
                    shell_output.append(line.strip('\n'))

        return shell_output

    def close_connection(self):
        write_to_log('SSH: Closing Connection')
        self.ssh.close()

    def get_version(self):
        v = self.exec_command('system resource print', False)
        return str(v[1]).strip()

    def get_fw_version(self):
        v = self.exec_command('system routerboard print', False)
        return str(v[6]).strip()

    def get_pppoe(self):
        pppoe = self.exec_command('interface pppoe-client print', False)
        pppoe_position = str(pppoe).find('user=')
        end_pppoe_position = str(pppoe).find(' password')
        pppoe_user = str(pppoe)[pppoe_position + 5:end_pppoe_position]
        # return str(v[1]).strip()
        return pppoe_user.strip(' "')

    def get_identity(self):
        identity = self.exec_command('system identity print', False)
        identity_position = str(identity).find('name: ')
        name = str(identity)[identity_position + 6:-10]
        return name.replace(" ", "-")

    def online_update(self):
        self.exec_command([
            'ip dns set servers=189.45.192.3,177.200.200.20'
            'system package update set channel=long-term',
            'system package update check-for-updates',
            'system package update install'
        ], True)
    def get_architecture(self):
        resource = self.exec_command('system resource print', False)
        architecture_position = str(resource).find('architecture-name: ')
        board_name_postition = str(resource).find('board-name:')
        architecture = str(resource)[architecture_position + 19:board_name_postition - 21]
        return architecture


    def upload(self, version):
        filename = 'routeros/routeros-{0}-{1}.npk'.format(self.get_architecture(), version)

        def progress4(filename, size, sent, peername):
            write_to_log("(%s:%s) %s's progress: %.2f%%   \r" % (
            peername[0], peername[1], filename, float(sent) / float(size) * 100))

        write_to_log('SCP: Opening Connection to host {0}@{1}:{2}'.format(self.user, self.host, self.port))
        scp = SCPClient(self.ssh.get_transport(), progress4=progress4)

        scp.put(filename)
        write_to_log('SCP: Closing Connection')
        scp.close()

    def offline_update(self, version):
        self.upload(version)
        self.exec_command('system reboot', False)

    def update_fw(self):
        self.exec_command([
            'system routerboard upgrade',
            'system reboot'
        ], True)

    def disable_ipv6(self):
        self.exec_command([
            'system package disable ipv6',
            'system reboot'
        ], True)

    def backup(self, file_name):
        def progress(filename, size, sent):
            write_to_log("%s's progress: %.2f%%   \r" % (filename, float(sent) / float(size) * 100))

        def progress4(filename, size, sent, peername):
            write_to_log("(%s:%s) %s's progress: %.2f%%   \r" % (
            peername[0], peername[1], filename, float(sent) / float(size) * 100))
        '''
        if self.DebugLevel==2:
            scp = SCPClient(self.ssh.get_transport(), progress=progress)

        if self.DebugLevel==3:
            scp = SCPClient(self.ssh.get_transport(), progress4=progress4)

        if self.DebugLevel<=1:
            scp = SCPClient(self.ssh.get_transport())
        '''
        write_to_log('SCP: Opening Connection to host {0}@{1}:{2}'.format(self.user, self.host, self.port))
        scp = SCPClient(self.ssh.get_transport(), progress4=progress4)

        self.exec_command('system backup save name={0}'.format(file_name), False)


        scp.get('{0}.backup'.format(file_name))
        write_to_log('SCP: Closing Connection')
        scp.close()

    def create_vpn(self):
        pass

    def create_vpls(self):
        pass


def try_connect(host, Ports, Users, Passwords, DebugLevel):
    connection_error = None

    # try each port
    for port in Ports:

        # try each user
        for user in Users:
            connection_error = False

            # try password
            for password in Passwords:
                t = RbUpdater(host, port, user, password, DebugLevel).connect()

                # se conectar, para
                if is_connected(t):
                    write_to_log('Conectado em {0}@{1}:{2}'.format(user, host, port))
                    if DebugLevel >= 1:
                        print('Conectado em {0}@{1}:{2}'.format(user, host, port))
                    return t

                # se der erro de conexão,
                # para as tentativas de senha e sobe pro nível de usuários
                if t == 'connection error':
                    write_to_log('Falha ao se conectar em {0}@{1}:{2}'.format(user, host, port))
                    connection_error = True
                    break
            if connection_error:
                break
    write_to_log("Todas as tentativas realizadas, não foi possível se conectar ao host {0}".format(host))
    if DebugLevel >= 1:
        print("Todas as tentativas realizadas, não foi possível se conectar ao host {0}".format(host))
    return False


def is_connected(connection):
    if type(connection) == RbUpdater:
        return True
    else:
        return False









