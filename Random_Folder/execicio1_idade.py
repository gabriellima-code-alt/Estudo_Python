

nome1 = input("Digite um nome: ")
nome2 = input("Digite um nome: ")
idade1 = int(input("Digite a idade do primeiro usúario: "))
idade2 = int(input("Digite a idade do segundo usúario: "))

if idade1 > idade2:
    print (f"O(A) {nome1} de {idade1} anos, é mais velho que O(A){nome2} de {idade2} anos.")
elif idade1 < idade2:
   print (f"O(A) {nome1} de {idade1} anos, é mais novo que O(A){nome2} de {idade2} anos.")
    
else:
     print(f"O(A) {nome1} de {idade1} anos, tem a mesma idade que O(A){nome2} de {idade2} anos.")