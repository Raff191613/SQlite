import sqlite3
import time
secret = "123456"

senha = input("Digite sua senha:")
if senha != secret:
    print("Senha invalida, encerrando...")
    time.sleep(1)
    
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service  TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("*************************")
    print("SEJA BEM VINDO. \n i: Inserir senha \n l: Listar serviços salvos \n r: Recuperar senha \n s: Sair")
    print("*************************")

def get_password(user):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("serviço não cadastrado.")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_passwords(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("Qual opção desejada?: ")
    if op not in [ 'i', 'l', 'r', 's']:
        print("Opção invalida.")
        continue
    if op == 's':
        print("Encerrando..")
        time.sleep(1)
        break
    if op == 'i':
        service = input('Qual o nome do serviço?: ')
        username = input('Qual o nome de usuário?: ')
        password = input('Qual a senha?: ')
        insert_passwords(service, username, password)
    if op == 'l':
        show_services()
    if op == 'r':
        service = input("Qual o serviço que deseja ter a senha?")
        get_password(service)

conn.close
        