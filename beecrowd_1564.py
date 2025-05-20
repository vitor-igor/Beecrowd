import sys

entrada = [int(x) for x in sys.stdin.read().splitlines()]
indice = 0

while True:
    if indice >= len(entrada):
        break

    if entrada[indice] == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")

    indice += 1