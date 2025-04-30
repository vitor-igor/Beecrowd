lista_numeros_pares = []

for i in range(5):
    numero = int(input())
    if ((numero % 2) == 0):
        lista_numeros_pares.append(numero)

print(f"{len(lista_numeros_pares)} valores pares")