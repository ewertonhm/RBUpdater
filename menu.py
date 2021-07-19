from txt_rw import *
from pathlib import *
from pasta import create_routeros_folder
import consolemenu



def main_menu():
    print("[1] Realizar Backup.")
    print("[2] Verificar a versão do RouterOS.")
    print("[3] Verificar a versão do Firmware.")
    print("[4] Realizar Backup e verificar a versão do RouterOS e Firmware")
    print("[5] Atualizar RouterOS.")
    print("[6] Atualizar Firmware.")

    #print("[7] Criar VPLS.")
    #print("[8] Criar VPN.")
    #print("[9] Desabilitar IPv6.")
    print("[0] Close.")
    option = input('Escolha uma opção: ')
    return option

def hosts_menu():
    print("Como deseja inserir os IPs:")
    print("[1] Ler arquivo txt")
    print("[2] Inserir manualmente")
    print()
    option = input('Escolha uma opção: ')
    return option

def menu_txt():
    file = input("Insira o nome do arquivo: ")
    return file

def menu_manual(mensagem):
    stop = False
    ips = []
    while not stop:
        ip = input(mensagem)
        if ip != 'zero' and ip != '0':
            ips.append(ip)
        else:
            stop = True
    return ips

def users_menu(Users):
    print("Tentativas de conexão serão feitas utilizando o(s) seguinte(s) usuário(s):")
    for user in Users:
        print(user)
    print()
    print("Deseja inserir mais algum usuário?")
    print("[1] Ler arquivo txt")
    print("[2] Inserir manualmente")
    print("[0] Não")
    option = input('Escolha uma opção: ')
    return option

def passwords_menu(Passwords):
    print("Tentativas de conexão serão feitas utilizando a(s) seguinte(s) senha(s):")
    for pwd in Passwords:
        print(pwd)
    print()
    print("Deseja inserir mais alguma senha?")
    print("[1] Ler arquivo txt")
    print("[2] Inserir manualmente")
    print("[0] Não")
    option = input('Escolha uma opção: ')
    return option

def ports_menu(Ports):
    print("Tentativas de conexão serão feitas utilizando a(s) seguinte(s) porta(s):")
    for port in Ports:
        print(port)
    print("Deseja inserir mais alguma porta?")
    print("[1] Sim")
    print("[0] Não")
    option = input('Escolha uma opção: ')
    return option

def update_menu():
    print("Como deseja realizar a atualização:")
    print("[1] Atualizar para a ultima versão LTS via internet")
    print("[2] Enviar arquivos")
    print()
    option = input('Escolha uma opção: ')
    return option

def version_menu():
    folder = create_routeros_folder()
    folder = str(folder) + "\\routeros\\"
    print("Obs: Necessário inserir manualmente os arquivos 'npk' na pasta {0}".format(folder))
    version = input("Insira a versão que você irá instalar (exemplo: 6.47.10): ")
    return version