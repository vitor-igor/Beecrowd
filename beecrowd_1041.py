def quadrante_ponto(posicao_x: float, posicao_y: float) -> str:
    if posicao_x == 0 and posicao_y == 0:
        return "Origem"
    elif posicao_x > 0 and posicao_y > 0:
        return "Q1"
    elif posicao_x < 0 and posicao_y > 0:
        return "Q2"
    elif posicao_x < 0 and posicao_y < 0:
        return "Q3"
    elif posicao_x > 0 and posicao_y < 0:
        return "Q4"
    elif posicao_x == 0 and posicao_y != 0:
        return "Eixo Y"
    elif posicao_x != 0 and posicao_y == 0:
        return "Eixo X"

posicao_x, posicao_y = input().split()

posicao_x = float(posicao_x)
posicao_y = float(posicao_y)

quadrante = quadrante_ponto(posicao_x, posicao_y)

print(quadrante)