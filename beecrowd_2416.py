percurso, comprimento_pista = [int(i) for i in input().split()]

if (percurso % comprimento_pista) == 0:
    print("0")
else:
    ponto_termino = percurso % comprimento_pista
    print(ponto_termino)