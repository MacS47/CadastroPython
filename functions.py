# ------------------------
# A primeira etapa consiste em exibir o menu de de opções:
# * Cadastrar
# * Editar
# * Listar
# * Sair

import os, sqlite3

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

# A função solicita que o usuário informe os dados pessoais, caso o usuário 
# informe CPF já existente a função é encerrada
def register():

    # Limpando a tela
    clear()
    
    # Inicializado a conexão ao banco SQLite e 
    # instanciando um cursor
    connection = sqlite3.connect("cadastro.db")
    cursor = connection.cursor()

    # Solicitando dados do usuário
    print(f"\n====== DADOS PESSOAIS ======\n")
    nome = input(f"\nInforme o seu nome completo: ")
    idade = int(input(f"\nInforme a sua idade: "))
    cpf = int(input(f"\nInforme o seu cpf(sem pontos e sem hífen): "))

    # Buscando todos os dados de usuários no banco cadastro.db
    # e armazenando na variável result_set_usuario
    cursor.execute("""SELECT * FROM usuario""")    
    result_set_usuario = cursor.fetchall()

    # Percorrendo os dados da variável para identificar se o CPF
    # informado pelo usuário já encontra-se na base
    for items in result_set_usuario:
        if(items[3] == cpf):
            verificador_cpf = False
        else:
            verificador_cpf = True
    
    # Caso o CPF ainda não tenha sido cadastrado, os dados serão inseridos no banco de dados
    if(verificador_cpf):
        cursor.execute("""
            INSERT INTO usuario(nome,idade,cpf)
            VALUES(?,?,?)
        """,
        (nome,idade,cpf))
        
        # O trecho abaixo foi criado para obter o ID do usuário inserido anteriormente.
        # É necessária essa informação para cadastrar o endereço do mesmo e vincular ao usuário
        cursor.execute("""SELECT * FROM usuario""")    
        result_set_usuario = cursor.fetchall()

        for items in result_set_usuario:
            if(items[1] == nome):
                id_usuario = items[0]

        # Inicializanda a entrada de dados de endereço
        print(f"\n==== ENDEREÇO ====\n")
        rua = input(f"\nInforme a rua: ")
        numero = int(input(f"\nInforme o número: "))
        bairro = input(f"\nInforme o bairro: ")
        cidade = input(f"\nInforme a cidade: ")
        complemento = input(f"\nInforme o complemento se houver: ")
        uf = input(f"\nInforme a UF: ")
        
        # Inserindo o endereço informado pelo usuário e vinculando ao cadastro da tabela usuario
        cursor.execute("""
            INSERT INTO endereco(rua,numero,bairro,cidade,complemento,uf,id_usuario)
            VALUES(?,?,?,?,?,?,?)
        """,
        (rua,int(numero),bairro,cidade,str(complemento),uf,int(id_usuario)))
    
    # Caso o cpf informado já encontra-se na base, a rotina abaixo será executada
    else:
        print("\n\n\t\t\tAtenção!\nCPF já cadastrado.\nCaso você deseje editar um registro acesse o menu 2 - EDITAR.")

    # Realizando o commit dos dados inseridos no banco
    # e fechando a conexão
    connection.commit()
    connection.close()

    # Informando ao usuário que ele será redirecionado ao menu
    input(f"\n\nVocê será redirecionado para o menu principal.\nPressione Enter.")

def edit():
    print(f"\nNesse menu você poderá selecionar um registro e editá-lo.")
    input(f"\nVocê será redirecionado para o menu principal.\nPressione Enter.")


# A função realiza uma busca de todos os usuários que possuem endereço, cadastrados na base
def list():

    # Realizando a limpeza da tela
    clear()

    # Inicializando a conexão ao banco cadastro.db
    # e instanciando um cursor
    connection = sqlite3.connect('cadastro.db')
    cursor = connection.cursor()

    # Buscando todos os usuários que possuam endereço, no banco de dados
    cursor.execute("""
        SELECT u.nome, u.idade, u.cpf, e.rua, e.numero, e.bairro, e.cidade, e.uf
        FROM usuario u, endereco e
        WHERE u.id_usuario = e.id_usuario
    """)

    # Armazenando o resultado na variável result_set_all
    result_set_all = cursor.fetchall()

    # Informando ao usuário o número de usuário com endereço cadastrado
    # e logo abaixo exibindo os dados.
    print(f"Total de usuários com endereços cadastrados: {len(result_set_all)}")
    print(f"\n==============================================\n")
    print(f"NOME, IDADE, CPF, RUA, NUMERO, BAIRRO, CIDADE, UF")
    for items in result_set_all:
        print(items)

    # Realizando o commit dos dados inseridos no banco
    # e fechando a conexão
    connection.commit()
    connection.close()
    
    # Informando ao usuário que ele será redirecionado ao menu
    input(f"\nVocê será redirecionado para o menu principal.\nPressione Enter.")
    
# A função menu é utilizada para informar as tarefas disponíveis no programa e
# direcionar o usuário para a função desejada
def menu():
    option = -1
    while option != 0:
        clear()
        print("====== MENU PARA CADASTRO ======\n")
        print("1 - CADASTRO")
        print("2 - EDIÇÃO")
        print("3 - RELATÓRIO")
        print("0 - SAIR\n")
        option = int(input("Qual menu você deseja acessar: "))
        if option > 0 and option < 4:
            switch_case(option)
        elif option < 0 or option > 3:
            input(f"\nVocê informou um valor inválido!\nPressione Enter para continuar.")
    print(f"\nVocê selecionou a opção {option}.\nO programa será encerrado.\n")