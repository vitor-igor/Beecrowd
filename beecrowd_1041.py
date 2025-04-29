posicao_x, posicao_y = input().split()

posicao_x = float(posicao_x)
posicao_y = float(posicao_y)

if posicao_x == 0 and posicao_y == 0:
    print("Origem")
elif posicao_x > 0 and posicao_y > 0:
    print("Q1")
elif posicao_x < 0 and posicao_y > 0:
    print("Q2")
elif posicao_x < 0 and posicao_y < 0:
    print("Q3")
elif posicao_x > 0 and posicao_y < 0:
    print("Q4")
elif posicao_x == 0 and posicao_y != 0:
    print("Eixo Y")
elif posicao_x != 0 and posicao_y == 0:
    print("Eixo X")