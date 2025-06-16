abas, qtde_acoes = [int(x) for x in input().split()]

for i in range(qtde_acoes):
    acao = input()

    if acao == "fechou":
        abas += 1
    elif acao == "clicou":
        abas -= 1

print(abas)