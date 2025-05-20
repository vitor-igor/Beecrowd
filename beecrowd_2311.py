qtde = int(input())

for i in range(qtde):
    media = 0
    nome = input()
    dificuldade = float(input())
    notas = [float(x) for x in input().split()]

    notas.remove(max(notas))
    notas.remove(min(notas))

    for j in range(5):
        media += notas[j] * dificuldade

    print(f"{nome} {media:.2f}")