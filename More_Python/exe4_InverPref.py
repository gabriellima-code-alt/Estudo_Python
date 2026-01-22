

like_series = input("Você gosta de séries? (s/n): ")
gosta = (like_series == "s")

if not gosta:
    print("Talvez você prefira filmes")
else:
    print("Ótimo, você é do time das séries")