
import json

caminho = 'Modelagem/arquivo.json'

def listarFuncionario():
    with open(caminho, 'r') as f:
        lista = json.load(f)

    return lista

def verFuncionario():

    listaFuncionarios = listarFuncionario()

    print("Lista de Funcionários: ")

    print("ID | Nome     | Sigla  |  Sálario")

    for funcionario in listaFuncionarios:

        print(
            f'{funcionario["ID_Funcionario"]} | {funcionario["Nome"]} | {funcionario["salario"]} | {funcionario["Sigla_Departamento"]} | {funcionario["Salário"]}')

    input()



while True:

    print('''
    Bem vindo a Empresa XYZ
    Menu:
    1. Ver Funcionários
    2. Inserir Funcionário
    0. Sair
    
    ''')

    op = input("Escolha uma opção: ")

    match op:
        case "1":
            verFuncionario()

        case "0":
            print("Saindo do Programa...")
            break















