#Calculadora
#Por Daniels :D

import os
os.system("cls")

print("CALCULADORA")
print("\nMenu de opções:\n\n1 - Somar dois números.\n2 - Multiplicar dois números.\n3 - Subtrair dois números.\n4 - Dividir dois números.")
x = int(input("\nEscolha a opção desejada: "))
if x >= 1 and x <= 4:
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    match x:
        case 1:
            r = n1 + n2
            print(f"\nResultado: {r}")
        case 2:
            r = n1 * n2
            print(f"\nResultado: {r}")
        case 3:
            r = n1 - n2
            print(f"\nResultado: {r}")
        case 4:
            if n2 != 0:
                r = n1 / n2
                print(f"\nResultado: {r}")
            else:
                print("\nNão é possível dividir um número por 0.")
else:
    print("\nOPÇÃO INVÁLIDA")