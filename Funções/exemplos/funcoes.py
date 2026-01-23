#Exemplo 1
def saudacao():
    print("Olá, Bem-Vindo(a) ao sistema!")
    print("Aqui você pode treinar Python e lógica")


saudacao()

#--------------------------------------------------------------------------

#Exemplo 2

def saudacao_personalizada(nome):
    print("Olá", nome, "! Seja Bem-Vindo(a)!!")


nome = input ("Digite seu nome: ")
saudacao_personalizada(nome)

#-------------------------------------------------------------------

# Exemplo 3

def somar (x, y):
    resultado = x + y
    return resultado

x = somar (3, 5)
print("Resultado da soma 1:", x)

y = somar (10, 20)
print(" Resultado da soma 2:", y)


#---------------------------------------------------------

#Exemplo 4

def calcular_media (n1,n2,n3): 
    media = (n1 + n2 + n3) /3
    return media

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = calcular_media(n1,n2,n3)

print("Média: ", media)

if media >= 7:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")

#-------------------------------------------------------
#def cadastrar_serie(lista_series):
 #nome = input("Digite o nome da série: ")
 #lista_series.append(nome)
 #print("Série cadastrada com sucesso")


#nome = input("Digite o nome da série: ")
#cadastrar_serie(lista_series)


#def listar_series(lista_series):
    #print("\nSéries cadastradas: ")
#if len(listar_series) == 0:
    #print("Nenhuma série cadastrada ainda.")
#else:
    #for i in range(len(listar_series)):
        #print(f"{i+1} - {listar_series[i]}")
        #series = []
    #while True:
     #cadastrar_serie(series)
     #listar_series(series)
     #continuar = input("Deseja cadastrar outra série(s/n): ")
     #if continuar.lower() != 's':
       #break


#(cadastrar_serie(lista_series))
#(listar_series(lista_series))
#---------------------------------------------------------------

#Exemplo 5

