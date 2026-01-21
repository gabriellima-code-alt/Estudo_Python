

idade = int(input("idade: "))
estudando = input("é estudante?(s/n): ")

if idade < 18 or estudando == "s":
    print("Você tem direito a desconto.")
else:
    print("Você NÃO tem direito a desconto.")