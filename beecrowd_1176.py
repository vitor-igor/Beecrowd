def lista_fibonacci(posicao_final: int) -> list:
    lista = []
    for i in range(posicao_final):
        if i <= 1:
            lista.append(i)
        else:
            lista.append((lista[i - 2] + lista[i - 1]))
    return lista

posicoes = []

qtde = int(input())

for i in range(qtde):
    posicoes.append(int(input()))

lista = lista_fibonacci(max(posicoes) + 1)

for j in range(len(posicoes)):
    print(f"Fib({posicoes[j]}) = {lista[posicoes[j]]}")