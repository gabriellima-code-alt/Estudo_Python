
series = []
for i in range(1, 6):
    nova = input("Digite o nome de uma série: ")
    series.append(nova)

print("Série cadastradas: ")
for i in range(len(series)):
    print(f"{i+1} - {series[i]}")