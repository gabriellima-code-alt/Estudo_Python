

nome = input("Digite seu nome de usuário: ")
numero_episodios = int(input("Digite o número de episódios que assistiu hoje: "))

if numero_episodios == 0:
    print(f"Você não assistiu nada hoje, {nome}")
elif numero_episodios >= 3:
    print(f"Assistiu pouco hoje, {nome}")
elif numero_episodios >= 4:
    print(f"Boa maratona, {nome}")
elif numero_episodios > 8:
    print(f"Vai dormir, {nome}")
else:
    print("Valor Inválido")