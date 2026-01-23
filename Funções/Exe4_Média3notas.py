

def calcular_media (n1,n2,n3): 
    media = (n1 + n2 + n3) /3
    return media

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = calcular_media(n1,n2,n3)

print("Média: ", media)

if media >= 7:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")