#Exemplo 1

series = ["Dark","Breaking Bad", "Dexter"]

print(series[0])
print(series[1])
print(series[2])

print("-------------------------------------------------")
#------------------------------------------------------------
#Exemplo 2

series = []

nova = input("Digite o nome de uma série: ")
series.append(nova)

print(series)

print("-------------------------------------------------")
#------------------------------------------------------------
#Exemplo 3

series = []
for i in range(3):
    nova = input("Digite o nome de uma série: ")
    series.append(nova)

print("Série cadastradas: ")
for s in series:
    print("-", s)

#------------------------------------------------------------
#Exemplo 4

series = ["Strager Thigs","Dexter","Filhos da Anarquia"]
for s in series:
    print(s)
#------------------------------------------------------------
#Exemplo 5

series = ["Breaking Bad", "Origem", "Rick and Morty"]
series.remove("Rick and Morty")
print(series)