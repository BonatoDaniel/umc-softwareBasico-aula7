#Cálculo da conta final de um hóspede
#Por Daniels :D

import os
os.system("cls")

print("CONTA FINAL DO HÓSPEDE")
nh = str(input("\nNome do hóspede: "))
ta = str(input("Tipo de apartamento: ")).upper()
if ta == "A" or ta == "B" or ta == "C" or ta == "D":
    nd = int(input("Número de diárias: "))
    if nd > 0:
        match ta:
            case "A":
                vd = 150
            case "B":
                vd = 100
            case "C":
                vd = 75
            case "D":
                vd = 50
        vtd = vd * nd
        print("Valor Total das Diárias: R$", vtd)
        ci = float(input("Consumo interno: "))
        if ci >= 0:
            s = vtd + ci
            ts = s * 0.1
            tg = s + ts
            print(f"\nSubtotal: R${s:.2f}\nTaxa de Serviço: R${ts:.2f}\n\nTotal Geral: R${tg:.2f}")
        else:
           print("\nVALOR INVÁLIDO.")
    else:
        print("\nVALOR INVÁLIDO.")
else:
    print("\nVALOR INVÁLIDO.")