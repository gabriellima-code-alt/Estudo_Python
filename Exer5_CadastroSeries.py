
series = []

for i in range (0, 5):
    nova = input("Digite o nome de uma série:")
    series.append(nova)
    
print("As séries cadastradas foram: ")
for s in series:
    print(f"- {s}")
