import json
import os

arquivo = 'alunos.json'

def cadastro():
    import datetime
    import re

    print('\033[36mVocê escolheu a opção de cadastro!\033[0m')
    while True:
        nome = input('\033[36mDigite seu nome completo: \033[0m').strip()
        if len(nome) >= 10:
            nome = nome
            break
        print('\033[1;31mNome muito curto! Digite o nome completo!\033[0m')
    while True:
        nome_user = input('\033[36mDigite seu nome de usuário: \033[0m').strip()
        if nome_user:
            break
        print('\033[1;31mNome de usuário inválido!\033[0m')
    while True:
        idade = input('\033[36mDigite sua idade: \033[0m').strip()
        if idade.isdigit():
            break
        print('\033[1;31mIdade inválida! Digite um número inteiro.\033[0m')
    while True:
        email = input('\033[36mDigite seu email: \033[0m').strip()
        if '@' in email and '.' in email:
            break
        print('\033[1;31mEmail inválido!\033[0m')
    while True:
        senha = input('\033[36mDigite sua senha (mínimo 8 caracteres e 1 caractere especial): \033[0m')
        if len(senha) < 8:
            print('\033[1;31mSenha muito curta!\033[0m')
            continue
        if not re.search(r'[^a-zA-Z0-9]', senha):
            print('\033[1;31mA senha deve conter pelo menos um caractere especial (ex: !, @, #, etc)\033[0m')
            continue
        break
    data_registro = datetime.date.today().isoformat() 

    novo_aluno = {
        'nome': nome,
        'nome_user': nome_user,
        'idade': int(idade),  
        'email': email,
        'senha': senha,
        'registro': data_registro
    }

    dados = carregar_dados()  
    dados.append(novo_aluno)
    salvar_dados(dados)      

    print(f'\033[36mUsuário {nome}, cadastrado com sucesso!\033[0m')


def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo,'r') as f:
            return json.load(f)
    return []

def salvar_dados(lista_alunos):
    with open(arquivo, 'w') as f:
        json.dump(lista_alunos, f, indent=4)

