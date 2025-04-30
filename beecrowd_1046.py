inicio, fim = input().split()

inicio = int(inicio)
fim = int(fim)

tempo_jogado = 0

if (inicio > fim):
    tempo_jogado = 24 - inicio
    tempo_jogado += fim
elif (inicio == fim):
    tempo_jogado = 24
else:
    tempo_jogado = fim - inicio
	
print(f"O JOGO DUROU {tempo_jogado} HORA(S)")