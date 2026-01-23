def conta_dez(num):
lista = []
contador = 0
for i in range (5):
  lista.append(num)
for n in lista:
 if n > 10:
    contador += 1
print("Números Maiores que 10: ", contador)



num = int(input(f"Digite um Número inteiro: "))
conta_dez(num)
