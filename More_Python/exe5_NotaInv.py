

nota = float(input("DIgite uma nota de 0 a 10:"))

if not nota >= 0 and nota <= 10:
    print("Nota Inválida")
elif nota > 10:
    print("Nota Inválida")
else:
    print(f"Nota Registrada: {nota}")