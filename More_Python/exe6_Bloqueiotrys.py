

tentativas = int(input("Quantas tentativas você tem? \n"))
tem_tentativas = tentativas > 0

if not tem_tentativas:
    print("Sua conta está bloqueada")
else:
    print("Você ainda pode tentar fazer login")