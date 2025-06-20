while True:
    try:
        atributos = int(input())

        qtde_marcos, qtde_leo = [int(x) for x in input().split()]

        cartas_marcos, cartas_leo = [], []

        for i in range(qtde_marcos):
            cartas_marcos.append([int(x) for x in input().split()])

        for i in range(qtde_leo):
            cartas_leo.append([int(x) for x in input().split()])

        escolha = [int(x) for x in input().split()]

        escolha_marcos = cartas_marcos[escolha[0] - 1]
        escolha_leo = cartas_leo[escolha[1] - 1]

        atributo = int(input())

        if escolha_marcos[atributo - 1] > escolha_leo[atributo - 1]:
            print("Marcos")
        elif escolha_marcos[atributo - 1] < escolha_leo[atributo - 1]:
            print("Leonardo")
        elif escolha_marcos[atributo - 1] == escolha_leo[atributo - 1]:
            print("Empate")

    except EOFError:
        break