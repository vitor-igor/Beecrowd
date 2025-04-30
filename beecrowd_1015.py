def distancia_entre_dois_pontos(x1: float, x2: float, y1: float, y2: float) -> float:
  """
  Calcula a distância entre dois pontos quaisquer do plano cartesiano a partir dos pares ordenados de localização.

  Parâmetro:
  - x1 (float): Posição do primeiro ponto no eixo das abscissas (X).
  - x2 (float): Posição do segundo ponto no eixo das abscissas (X).
  - y1 (float): Posição do primeiro ponto no eixo das abscissas (Y).
  - y2 (float): Posição do segundo ponto no eixo das abscissas (Y).

  Retorno:
  - float: Valor da distância entre os dois pontos.
  """
  px = x2 - x1
  py = y2 - y1
  distancia = (px ** 2 + py ** 2) ** (1/2)
  return distancia

posicao_x1, posicao_y1 = input().split()
posicao_x2, posicao_y2 = input().split()

posicao_x1 = float(posicao_x1)
posicao_x2 = float(posicao_x2)
posicao_y1 = float(posicao_y1)
posicao_y2 = float(posicao_y2)

distancia = distancia_entre_dois_pontos(posicao_x1, posicao_x2, posicao_y1, posicao_y2)

print(f"{distancia:.4f}")