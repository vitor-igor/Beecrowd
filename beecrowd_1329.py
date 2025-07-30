jogo = {
    0: 0,
    1: 0
}

while True:
    qtde = int(input())

    if qtde == 0:
        break
    
    lista = [int(x) for x in input().split()]

    jogo[0] = lista.count(0)
    jogo[1] = lista.count(1)

    print(f"Mary won {jogo[0]} times and John won {jogo[1]} times")