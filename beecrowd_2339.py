competidores, folhas_compradas, folhas_competidor = [int(x) for x in input().split()]

folhas_faltantes = folhas_compradas - (folhas_competidor * competidores)

if folhas_faltantes >= 0:
    print('S')
else:
    print('N')