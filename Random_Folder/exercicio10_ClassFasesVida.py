#0 a 12 criança 
#13 a 17 adolecente 
#18 a 59 adulto 
#60+ idoso 
#mostra idade e classificação

idade = int(input("Digite sua Idade:"))

if idade >=0 and idade <= 12:
    print(f"Idade: {idade}; Classificação: Criança;")
elif idade >=13 and idade <=17:
    print(f"Idade: {idade}; Classificação: Adolecente;")
elif idade >=18 and idade <= 59:
    print(f"Idade: {idade}; Classificação: Adulto;")
elif idade >= 60:
    print(f"Idade: {idade}; Classificação: Idoso;")
else:
    print("Idade Inválida")
