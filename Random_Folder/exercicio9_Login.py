

username = input("Digite a o nome de usuário:")
senha = input("Digite a senha de usuário:")

if username == ("Admin") and senha == ("1234"):
    print("Login Realizado com Sucesso")
elif username != ("Admin"):
    print("Usuário não encontrado")
elif senha != ("1234"):
    print("Senha Inválida")

