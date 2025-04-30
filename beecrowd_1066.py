lista_numeros_pares = []
lista_numeros_impares = []
lista_numeros_positivos = []
lista_numeros_negativos = []

for i in range(5):
    numero = int(input())
    if ((numero % 2) == 0):
        lista_numeros_pares.append(numero)
    else:
        lista_numeros_impares.append(numero)
    
    if numero > 0:
        lista_numeros_positivos.append(numero)
    elif numero < 0:
        lista_numeros_negativos.append(numero)

print(f"{len(lista_numeros_pares)} valor(es) par(es)")
print(f"{len(lista_numeros_impares)} valor(es) impar(es)")
print(f"{len(lista_numeros_positivos)} valor(es) positivo(s)")
print(f"{len(lista_numeros_negativos)} valor(es) negativo(s)")