qtde = int(input())

for i in range(qtde):
    raio1, raio2 = [int(x) for x in input().split()]

    raio_minimo = raio1 + raio2

    print(raio_minimo)