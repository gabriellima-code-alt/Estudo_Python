
nome_serie = input("Digite o nome da Série: ")
episodios_temporada = int(input("Digite o número de episódios da temporada: "))
episodios_assistidos = int(input("Digite o número de episódios assistidos: "))

if episodios_assistidos == 0:
    print(f"Você ainda não começou a série, {nome_serie}")
elif 0 < episodios_assistidos < episodios_temporada:
    print(f"Você está com a série, {nome_serie} em andamento")
elif episodios_assistidos == episodios_temporada:
    print(f"Você Terminou a série, {nome_serie}, Parábens!!!")
else:
    print("Valor Inválido")