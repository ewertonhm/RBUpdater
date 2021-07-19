from datetime import datetime
from relatorio import *
from rb_class import *
from menu import *
from txt_rw import *
import argparse

"""
# Initialize parser
parser = argparse.ArgumentParser(description='Automatização de backups e atualizações de dispositivos Routerbard')

# Adding arguments
parser.add_argument('-t', '--targets', nargs='+',  help = '<Required> Lista de hosts', required=True)
parser.add_argument('-u', '--users', nargs='+',  help = '<Optional> Usuários')
parser.add_argument('-s', '--passwords', nargs='+',  help = '<Optional> Senhas')
parser.add_argument('-p', '--ports', nargs='+',  help = '<Optional> Portas')
parser.add_argument('-d', '--debug',  help = '<Optional> Debug mode')



# Read arguments from command line
args = parser.parse_args()

print(args)
"""


Debug = True
LTS = 'version: 6.47.10 (long-term)'
FW = 'current-firmware: 6.47.10'

Hosts = [] #args.targets
Ports = [22]
Users = ['admin']
Passwords = ['glock9mm']

"""
if args.users != None:
    for user in args.users:
        Users.append(user)
if args.passwords != None:
    for pwd in args.passwords:
        Passwords.append(pwd)
if args.ports != None:
    for port in args.ports:
        Ports.append(port)


Host_connection = []
Host_connection_datetime = []
Host_pppoe = []
Host_identity = []
Host_version = []
Host_fw_version = []
Host_backup_name = []
Host_updated = []
Host_fw_updated = []

"""


if __name__ == '__main__':
    ################################################################
    ####################### LEITURA DE IPS #########################
    ################################################################
    option = hosts_menu()

    ## [1] Ler arquivo txt
    if option == '1':
        file_name = menu_txt()
        values = read_file(file_name)
        for value in values:
            Hosts.append(str(value.removesuffix("\n")))
        if Debug:
            print(Hosts)
    ## [2] Inserir manualmente
    elif option == '2':
        values = menu_manual('Insira um endereço de IP, Insira zero para parar: ')
        for value in values:
            Hosts.append(str(values.removesuffix("\n")))
        if Debug:
            print(Hosts)
    else:
        print("Opção inválida")
        exit()
    print()
    ################################################################
    ############ FIM LEITURA DE IPS ################################

    ################################################################
    ############ USUARIOS ##########################################
    option = users_menu(Users)

    ## [1] Ler arquivo txt
    if option == '1':
        file_name = menu_txt()
        values = read_file(file_name)
        for value in values:
            Users.append(str(value.removesuffix("\n")))
        if Debug:
            print(Users)


    ## [2] Inserir manualmente
    elif option == '2':
        values = menu_manual('Insira um Usuário, Insira zero para parar: ')
        for values in values:
            Users.append(str(values.removesuffix("\n")))
        if Debug:
            print(Users)
    print()
    ################################################################
    ############ FIM LEITURA DE USUÁRIOS ###########################

    ################################################################
    ############ SENHAS ############################################
    option = passwords_menu(Passwords)

    ## [1] Ler arquivo txt
    if option == '1':
        file_name = menu_txt()
        values = read_file(file_name)
        for value in values:
            Passwords.append(str(value.removesuffix("\n")))
        if Debug:
            print(Passwords)


    ## [2] Inserir manualmente
    elif option == '2':
        values = menu_manual('Insira uma senha, Insira zero para parar: ')
        for values in values:
            Passwords.append(str(values.removesuffix("\n")))
        if Debug:
            print(Passwords)
    print()
    ################################################################
    ############ PORTAS ############################################
    option = ports_menu(Ports)

    if option == '1':
        values = menu_manual('Insira uma porta, Insira zero para parar: ')
        for values in values:
            Ports.append(str(values.removesuffix("\n")))
        if Debug:
            print(Ports)
    print()
    ################################################################
    ############ FIM LEITURA DE PORTAS #############################

    ############ MENU PRINCIPAL ####################################

    run = True

    while run:
        option = main_menu()

        ## [1] Realizar Backup
        if option == '1':
            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter+1,len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 1)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)

                    # GET INFORMATIONS
                    Host_pppoe.append(ssh.get_pppoe())
                    Host_identity.append(ssh.get_identity())
                    Host_backup_name.append('{0}_{1}_{2}'.format(Host_identity[counter], Host_pppoe[counter], host))

                    # BACKUP
                    ssh.backup(Host_backup_name[counter])

                else:
                    Host_connection.append(False)
                    Host_pppoe.append('#')
                    Host_identity.append('#')
                    Host_backup_name.append('#')


                counter = counter + 1

            print()
            print_relatorio_backup(
                Hosts,
                Host_connection,
                Host_connection_datetime,
                Host_pppoe,
                Host_identity,
                Host_backup_name)

        ## [2] Verificar a versão do RouterOS
        elif option == '2':
            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter+1,len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 1)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)
                    Host_version.append(ssh.get_version())
                else:
                    Host_connection.append(False)

                counter = counter + 1
            print()
            print_relatorio_version(
                Hosts,
                Host_connection,
                Host_connection_datetime,
                Host_version)

        ## [3] Verificar a versão do Firmware
        elif option == '3':
            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 1)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)
                    Host_fw_version.append(ssh.get_fw_version())

                else:
                    Host_connection.append(False)

                counter = counter + 1
            print()
            print_relatorio_fw_version(
                Hosts,
                Host_connection,
                Host_connection_datetime,
                Host_fw_version)

        ## [4] Realizar Backup e verificar a versão do RouterOS e Firmware
        elif option == '4':

            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 3)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)

                    # GET INFORMATIONS
                    Host_pppoe.append(ssh.get_pppoe())
                    Host_identity.append(ssh.get_identity())
                    Host_backup_name.append('{0}_{1}_{2}'.format(Host_identity[counter], Host_pppoe[counter], host))
                    Host_version.append(ssh.get_version())
                    Host_fw_version.append(ssh.get_fw_version())

                    ssh.backup(Host_backup_name[counter])

                    if Debug:
                        print(Host_version[counter])
                        print(Host_fw_version[counter])

                    ssh.close_connection()
                else:
                    Host_connection.append(False)
                    Host_pppoe.append('#')
                    Host_identity.append('#')
                    Host_backup_name.append('#')
                    Host_version.append('#')
                    Host_fw_version.append('#')
                    Host_updated.append('#')
                    Host_fw_updated.append('#')

                counter = counter + 1

            print_relatorio(
                Hosts,
                Host_connection,
                Host_connection_datetime,
                Host_pppoe,
                Host_identity,
                Host_version,
                Host_fw_version,
                Host_backup_name)

        ## [5] Atualizar RouterOS
        elif option == '5':
            option = update_menu()

            # [1] Atualizar para a ultima versão LTS via internet
            if option == '1':
                Host_connection = []
                Host_connection_datetime = []
                Host_pppoe = []
                Host_identity = []
                Host_version = []
                Host_fw_version = []
                Host_backup_name = []
                Host_updated = []
                Host_fw_updated = []

                counter = 0

                for host in Hosts:
                    print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                    ssh = try_connect(host, Ports, Users, Passwords, 1)
                    Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                    if ssh != False:
                        Host_connection.append(True)
                        ssh.online_update()
                        Host_updated.append(True)
                    else:
                        Host_connection.append(False)
                        Host_updated.append(False)

                    counter = counter + 1
                print()
                print_relatorio_version_updated(
                    Hosts,
                    Host_connection,
                    Host_connection_datetime)

            # [2] Enviar arquivos
            if option == '2':
                version = version_menu()

                Host_connection = []
                Host_connection_datetime = []
                Host_pppoe = []
                Host_identity = []
                Host_version = []
                Host_fw_version = []
                Host_backup_name = []
                Host_updated = []
                Host_fw_updated = []

                counter = 0

                for host in Hosts:
                    print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                    ssh = try_connect(host, Ports, Users, Passwords, 1)
                    Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                    if ssh != False:
                        Host_connection.append(True)
                    else:
                        Host_connection.append(False)

                    counter = counter + 1

        ## [6] Atualizar Firmware
        elif option == '6':
            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 1)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)
                    ssh.update_fw()
                    Host_fw_updated.append(True)
                else:
                    Host_connection.append(False)

                counter = counter + 1
            print()
            print_relatorio_version_fw_updated(
                Hosts,
                Host_connection,
                Host_connection_datetime)

        ## [7] Criar VPLS
        elif option == '7':
            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 1)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)
                else:
                    Host_connection.append(False)

                counter = counter + 1

        ## [8] Criar VPN
        elif option == '8':
            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 1)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)
                else:
                    Host_connection.append(False)

                counter = counter + 1

        ## [9] Desabilitar IPv6
        elif option == '9':
            Host_connection = []
            Host_connection_datetime = []
            Host_pppoe = []
            Host_identity = []
            Host_version = []
            Host_fw_version = []
            Host_backup_name = []
            Host_updated = []
            Host_fw_updated = []

            counter = 0

            for host in Hosts:
                print("Host {0}/{1}".format(counter + 1, len(Hosts)))

                ssh = try_connect(host, Ports, Users, Passwords, 1)
                Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
                if ssh != False:
                    Host_connection.append(True)
                else:
                    Host_connection.append(False)

                counter = counter + 1

        ## [0] Close
        elif option == '0':
            break








    '''
    counter = 0

    for host in Hosts:
        ssh = try_connect(host, Ports, Users, Passwords, 3)
        Host_connection_datetime.append(datetime.now().strftime('%d/%m/%Y %H:%M'))
        if ssh != False:
            Host_connection.append(True)

            # GET INFORMATIONS
            Host_pppoe.append(ssh.get_pppoe())
            Host_identity.append(ssh.get_identity())
            Host_backup_name.append('{0}_{1}_{2}'.format(Host_identity[counter], Host_pppoe[counter], host))
            Host_version.append(ssh.get_version())
            Host_fw_version.append(ssh.get_fw_version())

            ssh.backup(Host_backup_name[counter])

            if Debug:
                print(Host_version[counter])
                print(Host_fw_version[counter])

            # UPDATE ROUTEROS
            if Host_version[counter] != LTS:
                ssh.update()
                Host_updated.append(True)
            else:
                if Debug:
                    print('RouterOS já está na ultima versão long-term')
                Host_updated.append(False)

            # UPDATE FIRMWARE
            if Host_fw_version[counter] != FW:
                ssh.update_fw()
                Host_fw_updated.append(True)
            else:
                if Debug:
                    print('Firmware já esta na ultima versão')
                Host_fw_updated.append(False)

            ssh.close_connection()
        else:
            Host_connection.append(False)
            Host_pppoe.append('#')
            Host_identity.append('#')
            Host_backup_name.append('#')
            Host_version.append('#')
            Host_fw_version.append('#')
            Host_updated.append('#')
            Host_fw_updated.append('#')

        counter = counter + 1

    print_relatorio(
            Hosts,
            Host_connection,
            Host_connection_datetime,
            Host_pppoe,
            Host_identity,
            Host_version,
            Host_fw_version,
            Host_backup_name,
            Host_updated,
            Host_fw_updated)
    '''