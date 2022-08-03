import sqlite3

def initialize_database():
    connection = sqlite3.connect("cadastro.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INT NOT NULL,
            cpf CHAR(11)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS endereco(
            id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
            rua TEXT NOT NULL,
            numero INT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            complemento TEXT,
            uf CHAR(2) NOT NULL,
            id_usuario INTERGER NOT NULL
        );
    """)

    # Criando tabelas de LOG
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS log_usuario(
            id_log_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INT NOT NULL,
            cpf CHAR(11),
            data DATETIME,
            info TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS log_endereco(
            id_log_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
            rua TEXT NOT NULL,
            numero INT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            complemento TEXT,
            uf CHAR(2) NOT NULL, 
            id_usuario INTERGER NOT NULL,
            data DATETIME,
            info TEXT
        );
    """)

    # Triggers para tabela usuario
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS insert_usuario AFTER INSERT ON usuario
        BEGIN
            INSERT INTO log_usuario(nome,idade,cpf,data,info) 
            VALUES(new.nome,new.idade,new.cpf,datetime('now'),'INSERT');
        END;
    """)

    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_usuario AFTER UPDATE ON usuario
        BEGIN
            INSERT INTO log_usuario(nome,idade,cpf,data,info) 
            VALUES(new.nome,new.idade,new.cpf,datetime('now'),'UPDATE');
        END;
    """)

    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS delete_usuario BEFORE DELETE ON usuario
        BEGIN
            INSERT INTO log_usuario(nome,idade,cpf,data,info) 
            VALUES(old.nome,old.idade,old.cpf,datetime('now'),'DELETE');
        END;
    """)

    # Triggers para tabela endereco
    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS insert_endereco AFTER INSERT ON endereco
        BEGIN
            INSERT INTO log_endereco(rua,numero,bairro,cidade,complemento,uf,id_usuario,data,info) 
            VALUES(new.rua,new.numero,new.bairro,new.cidade,new.complemento,new.uf,new.id_usuario,datetime('now'),'INSERT');
        END;
    """)

    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_endereco AFTER UPDATE ON endereco
        BEGIN
            INSERT INTO log_endereco(rua,numero,bairro,cidade,complemento,uf,id_usuario,data,info) 
            VALUES(new.rua,new.numero,new.bairro,new.cidade,new.complemento,new.uf,new.id_usuario,datetime('now'),'UPDATE');
        END;
    """)

    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS delete_endereco BEFORE DELETE ON endereco
        BEGIN
            INSERT INTO log_endereco(rua,numero,bairro,cidade,complemento,uf,id_usuario,data,info) 
            VALUES(old.rua,old.numero,old.bairro,old.cidade,old.complemento,old.uf,old.id_usuario,datetime('now'),'DELETE');
        END;
    """)
