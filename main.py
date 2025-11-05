from user import User
from sistem import find_patners

DB ="data.db"

def create():
    import sqlite3
    with sqlite3.connect(DB) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users(
            id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            passworld TEXT,
            subjects TEXT
            )""")
def main():
    create()
    print("---Sistema de Estudos---")
    while True:
        print("\n1 - Registrar\n2 - Login\n3 - Buscar Parceiro\n0 - Sair")
        op = input("> ")
        if op == "1":
            name = input("Nome: ")
            email = input("Email: ")
            passworld = input("Senha: ")
            subjects = input("Matérias (separe por vírgula): ").split(",")
            User.register(DB,name,email,passworld,subjects)
            print("Usuario registrado com sucesso!")
        elif op =="2":
            email=input("Email: ")
            passworld = input("Senha: ")
            user = User.login(DB,email,passworld)
            print("Login Bem-sucedido!" if user else "Credenciais inválidas.")
        elif op =="3":
            subject = input("Matéria: ")
            patners = find_patners( DB,subject)
            print("Parceiros encontrados:",patners)
        else:
            break

if __name__ == "__main__":
    main()