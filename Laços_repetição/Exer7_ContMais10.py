

lista = []
contador = 0

for i in range (5):
    num = int(input(f"Digite um Número inteiro: "))
    lista.append(num)

for n in lista:
 if n > 10:
  contador += 1

print("Números Maiores que 10: ", contador)