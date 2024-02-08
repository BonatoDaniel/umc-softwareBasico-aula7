#Consoante ou Vogal
#Por Daniels :D

import os
os.system("cls")

print("CONSOANTE OU VOGAL?")
x = input("\nInsira uma letra: ").upper()
if x >= "0" and x <= "9":
    print("\nValor numérico.")
else:
    match x:
        case "A" | "E" | "I" | "O" | "U":
            print("\nVogal.")
        case _:
            print("\nConsoante.")
