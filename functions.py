# ------------------------
# A primeira etapa consiste em exibir o menu de de opções:
# * Cadastrar
# * Editar
# * Listar
# * Sair

import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def switch_case(option):
    swt_cs={
        1 : register,
        2 : edit,
        3 : list
    }
    function = swt_cs.get(option)
    print (function())


def register():
    print(f"\nfuncão Register")
    input(f"\nVocê será redirecionado para o menu principal.\nPressione Enter.")


def edit():
    print(f"\nfuncão Edit")
    input(f"\nVocê será redirecionado para o menu principal.\nPressione Enter.")


def list():
    print(f"\nfuncão List")
    input(f"\nVocê será redirecionado para o menu principal.\nPressione Enter.")


def menu():
    option = -1
    while option != 0:
        clear()
        print("====== MENU PARA CADASTRO ======")
        print("1 - CADASTRO")
        print("2 - EDIÇÃO")
        print("3 - RELATÓRIO")
        #print("3 - RELATÓRIO")
        print("0 - SAIR\n")
        option = int(input("Qual menu você deseja acessar: "))
        if option > 0 and option < 4:
            switch_case(option)
        elif option < 0 or option > 3:
            input(f"\nVocê informou um valor inválido!\nPressione Enter para continuar.")
    print(f"\nVocê selecionou a opção {option}.\nO programa será encerrado.\n")