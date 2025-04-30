while (True):
    posicaoX, posicaoY = input().split()

    posicaoX = float(posicaoX)
    posicaoY = float(posicaoY)

    if posicaoX == 0 or posicaoY == 0:
        break
    elif (posicaoX >= 0) and (posicaoY >= 0):
        print("primeiro")
    elif (posicaoX <= 0) and (posicaoY >= 0):
        print("segundo")
    elif (posicaoX <= 0) and (posicaoY <= 0):
        print("terceiro")
    elif (posicaoX >= 0) and (posicaoY <= 0):
        print("quarto")