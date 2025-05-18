vetor = []

num = int(input())
valor = 0

for i in range(1000):
    vetor.append(valor)

    valor += 1

    if valor == num:
        valor = 0

    print(f"N[{i}] = {vetor[i]}")