
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print ("A média é: ", media)

if media >= 7:
    print("Aluno Aprovado")
elif media >=5:
    print("Aluno de Recuperação")
else:
    print("Aluno Reprovado")