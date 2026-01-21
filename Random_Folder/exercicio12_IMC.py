

peso = float(input("Digite seu Peso:"))
altura = float(input("Digite sua Altura:"))
#calculo imc peso/ (altura*altura)
# IMC < 18.5 = abaixo do peso  18.5 a 24.9 = peso normal >25 = Acima do peso.

imc = peso / (altura * altura)

if imc < 18.5:
    print("Seu IMC é:",imc)
    print("Abaixo do Peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Seu IMC é:",imc)
    print("Peso Normal")
else:
    print("Seu IMC é:",imc)
    print("Acima do Peso")