#regra pra aprovação nota maior que 7 e presença acima de 75.


nota_final = float(input("Digite a Nota Final do aluno:"))
porcentagem_presenca = float(input("Digite a Porcentagem de presença:"))

if nota_final >= 7 and porcentagem_presenca >= 75:
    print("Aluno Aprovado!!")
elif nota_final < 7 and porcentagem_presenca < 75:
    print("Aluno Reprovado, por falta e nota...")
elif nota_final < 7:
    print("Aluno Reprovado, por Nota.")
elif porcentagem_presenca < 75:
    print("Aluno Reprovado, por Falta.")



