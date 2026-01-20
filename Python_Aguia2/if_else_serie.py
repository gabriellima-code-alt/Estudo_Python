
total_episodios = int(input("Insira o Número de episódios da Temporada:"))
assistidos = int(input("Insira Quantos episódios Assistiu:"))

if assistidos >= total_episodios:
    print("Você já terminou a temporada, Parábens!!!")
else:
    faltam = total_episodios - assistidos
    print(f"Você ainda não terminou, faltam {faltam} episódios, continue assistindo!!")