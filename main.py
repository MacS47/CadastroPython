# -----------------------------------------------------------------------------------------------------
# Objetivo:
# O objetivo aqui é desenvolver um programa capaz de cadastrar, editar, listar/exibir dados de usuários
# de forma que mesmo encerrando o programa, os dados gravados permaneçam armazenados.
# 
#

# ------------------------
# A primeira etapa consiste em exibir o menu de opções:
# * Cadastrar
# * Editar
# * Listar
# * Sair



import functions as f
import database as db

# Essa é a chamada para inicializar o banco de dados,
# caso o banco já exista o nada acontece
db.initialize_database()

f.menu()