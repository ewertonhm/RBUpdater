from txt_rw import write_to_log

def print_relatorio_full(
        Hosts,
        Host_connection,
        Host_connection_datetime,
        Host_pppoe,
        Host_identity,
        Host_version,
        Host_fw_version,
        Host_backup_name,
        Host_updated,
        Host_fw_updated):

    counter = 0
    for host in Hosts:
        print(' ')
        print('## Host: {0}'.format(host))
        s = None

        if Host_connection[counter]:
            v = None
            f = None

            print('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            print('## Identificação do Host: {0}'.format(Host_identity[counter]))
            print('## Usuário PPPoE: {0}'.format(Host_pppoe[counter]))
            print('## Backup realizado, arquivo salvo com o nome: {0}.backup'.format(Host_backup_name[counter]))
            print('## Versão do RouterOS no momento do acesso: {0}'.format(Host_version[counter][9:]))
            print('## versão do Firmware no momento do acesso: {0}'.format(Host_fw_version[counter][18:]))
            if Host_updated[counter]:
                print('## Realizado atualização do RouterOS: Sim')
            else:
                print('## Realizado atualização do RouterOS: Não')
            if Host_fw_updated[counter]:
                print('## Realizado atualização do Firmware: Sim')
            else:
                print('## Realizado atualização do Firmware: Não')
        else:
            print('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))

        print(' ')
        counter = counter + 1

def print_relatorio(
        Hosts,
        Host_connection,
        Host_connection_datetime,
        Host_pppoe,
        Host_identity,
        Host_version,
        Host_fw_version,
        Host_backup_name):
    write_to_log("## RELATORIO")
    counter = 0
    for host in Hosts:
        write_to_log('## Host: {0}'.format(host))
        print('## Host: {0}'.format(host))

        if Host_connection[counter]:
            write_to_log('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            write_to_log('## Identificação do Host: {0}'.format(Host_identity[counter]))
            write_to_log('## Usuário PPPoE: {0}'.format(Host_pppoe[counter]))
            write_to_log('## Backup realizado, arquivo salvo com o nome: {0}.backup'.format(Host_backup_name[counter]))
            write_to_log('## Versão do RouterOS: {0}'.format(Host_version[counter][9:]))
            write_to_log('## versão do Firmware: {0}'.format(Host_fw_version[counter][18:]))
            print('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            print('## Identificação do Host: {0}'.format(Host_identity[counter]))
            print('## Usuário PPPoE: {0}'.format(Host_pppoe[counter]))
            print('## Backup realizado, arquivo salvo com o nome: {0}.backup'.format(Host_backup_name[counter]))
            print('## Versão do RouterOS: {0}'.format(Host_version[counter][9:]))
            print('## versão do Firmware: {0}'.format(Host_fw_version[counter][18:]))
        else:
            write_to_log('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))
            print('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))

        print()
        counter = counter + 1

def print_relatorio_backup(
        Hosts,
        Host_connection,
        Host_connection_datetime,
        Host_pppoe,
        Host_identity,
        Host_backup_name):
    write_to_log("## RELATORIO BACKUP")
    counter = 0
    for host in Hosts:
        write_to_log('## Host: {0}'.format(host))
        print('## Host: {0}'.format(host))
        s = None

        if Host_connection[counter]:
            write_to_log('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            write_to_log('## Identificação do Host: {0}'.format(Host_identity[counter]))
            write_to_log('## Identificação do Host: {0}'.format(Host_identity[counter]))
            write_to_log('## Usuário PPPoE: {0}'.format(Host_pppoe[counter]))
            print('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            print('## Identificação do Host: {0}'.format(Host_identity[counter]))
            print('## Usuário PPPoE: {0}'.format(Host_pppoe[counter]))
            print('## Backup realizado, arquivo salvo com o nome: {0}.backup'.format(Host_backup_name[counter]))
        else:
            write_to_log('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))
            print('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))

        print()
        counter = counter + 1

def print_relatorio_version(
        Hosts,
        Host_connection,
        Host_connection_datetime,
        Host_version):
    write_to_log("## RELATORIO BACKUP")
    counter = 0
    for host in Hosts:
        write_to_log('## Host: {0}'.format(host))
        print('## Host: {0}'.format(host))
        s = None

        if Host_connection[counter]:
            write_to_log('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            write_to_log('## Versão do RouterOS no momento do acesso: {0}'.format(Host_version[counter][9:]))
            print('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            print('## Versão do RouterOS no momento do acesso: {0}'.format(Host_version[counter][9:]))


        else:
            write_to_log('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))
            print('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))

        print()
        counter = counter + 1
def print_relatorio_fw_version(
        Hosts,
        Host_connection,
        Host_connection_datetime,
        Host_fw_version):
    write_to_log("## RELATORIO BACKUP")
    counter = 0
    for host in Hosts:
        write_to_log('## Host: {0}'.format(host))
        print('## Host: {0}'.format(host))
        s = None

        if Host_connection[counter]:
            write_to_log('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            write_to_log('## Versão do RouterOS no momento do acesso: {0}'.format(Host_fw_version[counter][9:]))
            print('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            print('## Versão do RouterOS no momento do acesso: {0}'.format(Host_fw_version[counter][18:]))


        else:
            write_to_log('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))
            print('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))

        print()
        counter = counter + 1
    write_to_log("## RELATORIO BACKUP")
    counter = 0
def print_relatorio_version_updated(
        Hosts,
        Host_connection,
        Host_connection_datetime):
    write_to_log("## RELATORIO BACKUP")
    counter = 0
    for host in Hosts:
        write_to_log('## Host: {0}'.format(host))
        print('## Host: {0}'.format(host))
        s = None

        if Host_connection[counter]:
            write_to_log('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            write_to_log('## Versão do RouterOS atualizada: Sim')
            print('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            print('## Versão do RouterOS atualizada: Sim')


        else:
            write_to_log('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))
            print('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))

        print()
        counter = counter + 1
def print_relatorio_version_fw_updated(
        Hosts,
        Host_connection,
        Host_connection_datetime):
    write_to_log("## RELATORIO BACKUP")
    counter = 0
    for host in Hosts:
        write_to_log('## Host: {0}'.format(host))
        print('## Host: {0}'.format(host))
        s = None

        if Host_connection[counter]:
            write_to_log('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            write_to_log('## Versão do RouterOS atualizada: Sim')
            print('## Tentativa de conexão em: {0} : Sucessful'.format(Host_connection_datetime[counter]))
            print('## Versão da firmware atualizada: Sim')


        else:
            write_to_log('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))
            print('## Tentativa de conexão em: {0} : Failed'.format(Host_connection_datetime[counter]))

        print()
        counter = counter + 1





