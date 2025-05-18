s = 1
contador = 1

lista_denominadores = []
lista_numeradores = []

for i in range(3, 40, 2):
    lista_numeradores.append(i)
    lista_denominadores.append(2 ** contador)
    contador += 1

for i in range(len(lista_numeradores)):
    s += (lista_numeradores[i]/lista_denominadores[i])

print(f"{s:.2f}")