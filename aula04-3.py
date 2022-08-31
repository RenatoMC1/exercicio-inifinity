usuario = input("Digite seu login: ")
senha = int(input("Digite sua senha: "))

if usuario == "admin" and senha == 619:
    print("acesso liberado!")
else:
    print("Acesso bloqueado")