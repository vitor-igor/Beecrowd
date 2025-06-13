def distancia(coordenadasA: list, coordenadasB: list) -> float:
    d = (((coordenadasB[0] - coordenadasA[0]) ** 2) + ((coordenadasB[1] - coordenadasA[1]) ** 2) + ((coordenadasB[2] - coordenadasA[2]) ** 2)) ** (1 / 2)

    return d

naves = int(input())

posicoes = []

for i in range(naves):
    posicoes.append([int(x) for x in input().split()])

for indice, elemento in enumerate(posicoes):
    dist = 9999
    for j, elemento2 in enumerate(posicoes):
        if indice == j:
            continue
        if distancia(elemento, elemento2) < dist:
            dist = distancia(elemento, elemento2)
            
    if dist <= 20:
        print('A')
    elif dist > 20 and dist <= 50:
        print('M')
    else:
        print('B')