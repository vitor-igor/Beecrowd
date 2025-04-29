qtde_positivos = 0

for i in range (6):
    numero = float(input())

    if numero > 0:
        qtde_positivos += 1

print(f"{qtde_positivos} valores positivos")