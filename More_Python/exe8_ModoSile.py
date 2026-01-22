

modo_silencioso = input("O celular está no modo silencioso?(s/n): ")

silencioso = (modo_silencioso == "s")

if not silencioso:
    print("Seu celular está fazendo barulho")
else:
    print("Seu celular está no silencioso")