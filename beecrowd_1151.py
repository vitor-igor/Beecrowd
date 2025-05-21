indice = int(input())

lista = [0, 1]

for i in range(1, indice - 1):
    lista.append((lista[i] + lista[i - 1]))

resultado = " ".join([str(i) for i in lista])

print(resultado)