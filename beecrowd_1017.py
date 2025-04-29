tempo_horas = int(input())
velocidade_media = int(input())

distancia = velocidade_media * tempo_horas

gasolina = distancia / 12

print(f"{gasolina:.3f}")