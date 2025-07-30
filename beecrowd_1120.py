while True:
    valor = input().split()

    if valor[0] == "0" and valor[1] == '0':
        break
    else:
        saida = valor[1].replace(valor[0], "")
        saida = saida.lstrip("0")

        if len(saida) == 0:
            saida = "0"

        print(saida)