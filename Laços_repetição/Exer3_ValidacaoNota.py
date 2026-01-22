nota = float(input("Digite uma nota (0 a 10): "))

while nota < 0 or nota > 10:
    print("Nota inválida! Tente novamente.")
    nota = float(input("Digite uma nota (0 a 10): "))

print(f"Nota válida inserida: {nota}")
