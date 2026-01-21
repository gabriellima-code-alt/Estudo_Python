

compra = float(input("Digite o valor da compra: "))


if compra < 50:

    print(f"O valor do frete é de R$10, sua compra no total deu, R$", compra + 10)
elif compra <= 100:

    print(f"O valor do frete é de R$5, sua compra no total deu, R$", compra + 5)
elif compra >= 101:
    
    print(f"Valor acima de R$100, sem Frete. Total: R${compra}")

    