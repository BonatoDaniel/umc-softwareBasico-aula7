#Mostrar cargo
#Por Daniels :D

import os
os.system("cls")

print("MOSTRAR CARGO")
c = int(input("\nCódigo: "))
if c >= 1 and c <= 5:
    match c:
        case 1:
            print("\nEscrituário.")
        case 2:
            print("\nSecretária.")
        case 3:
            print("\nCaixa.")
        case 4:
            print("\nGerente.")
        case 5:
            print("\nDiretor.")
else:
    print("\nCÓDIGO INVÁLIDO.")