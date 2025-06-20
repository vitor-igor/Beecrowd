qtde = int(input())

distancias = []

for i in range(qtde):
    tempo, velocidade = [int(x) for x in input().split()]

    distancias.append(tempo * velocidade)

distancia_total = sum(distancias)

print(distancia_total)