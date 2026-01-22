

hora_atual = int(input("Qual horário atual?(apenas horas inteiras): "))


if not (9 <=  hora_atual <=18 ):
    print("Loja Fechada.")
else:
    print("Loja Aberta.")
