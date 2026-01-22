

convite = input("Você é convidado?(s/n): ")
vip = input("Você é VIP?(s/n): ")

convidado = (convite == "s") 
confirm_vip = (vip == "s")

if not convite and vip:
    print("Acesso negado")
else:
    print("Acesso Liberado")