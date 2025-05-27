import sys

entrada = sys.stdin.read().splitlines()
indice = 0

while True:
    if indice == len(entrada):
        break
    qtde = entrada[indice]
    indice += 1
    lista_lesmas = [int(x) for x in entrada[indice].split()]
    indice += 1

    lesma_mais_veloz = max(lista_lesmas)

    if lesma_mais_veloz < 10:
        print(1)
    elif lesma_mais_veloz >= 10 and lesma_mais_veloz < 20:
        print(2)
    elif lesma_mais_veloz >= 20:
        print(3)