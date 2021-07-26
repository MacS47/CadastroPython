# ------------------------
# A primeira etapa consiste em exibir o menu de de opções:
# * Cadastrar
# * Editar
# * Listar
# * Sair

import os


# Essa função é responsável por limpar a tela do Console
# funciona em Windows e Linux
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# A função recebe um valor e, dependendo desse valor uma segunda 
# função é chamada. Como não existe o switch case em python desenvolvi
# esse método
def switch_case(option):
    swt_cs={
        1 : register,
        2 : edit,
        3 : list
    }
    function = swt_cs.get(option)
    print (function())


def register():
    clear()
    
    print(f"\n====== DADOS PESSOAIS ======\n")

    name = input(f"\nInforme o seu nome completo: ")
    age = int(input(f"\nInforme a sua idade: "))
    cpf = int(input(f"\nInforme o seu cpf(sem pontos e sem hífen): "))

    verificador_cep = "N"
    while verificador_cep == "n" or verificador_cep == "N":

        print(f"\n==== ENDEREÇO ====\n")

        end_rua = input(f"\nInforme a rua: ")
        end_numero = int(input(f"\nInforme o número: "))
        end_bairro = input(f"\nInforme o bairro: ")
        end_cidade = input(f"\nInforme a cidade: ")
        end_complemento = input(f"\nInforme o complemento se houver: ")
        end_complemento2 = input(f"\nInforme o complemento adicional: ")
        end_uf = input(f"\nInforme a UF: ")

        # Criei esse campo para verificar se os dados informados estavam corretos
        verificador_cep = input(f"\n\nOs dados acima estão corretos(S/N): ")

    # Armazenando dentro do dicionário, os dados informados pelo usuário
    data_user={
        "name" : name,
        "age" : age,
        "cpf" : cpf,
        "end_rua" : end_rua,
        "end_numero" : end_numero,
        "end_bairro" : end_bairro,
        "end_cidade" : end_cidade,
        "end_complemento" : end_complemento,
        "end_complemento2" : end_complemento2,
        "end_uf" : end_uf
    }

    # Abrindo o arquivo e gravando os dados nele    
    file = open("base.txt","a")
    file.write(f"{data_user['name']};{data_user['age']};{data_user['cpf']};{data_user['end_rua']};{data_user['end_bairro']};{data_user['end_cidade']};{data_user['end_complemento']};{data_user['end_complemento2']};{data_user['end_uf']}\n")
    file.close()

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