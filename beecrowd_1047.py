def transformar_tempo_em_minutos(hora: int, minuto: int) -> int:
    return (hora * 60 + minuto)

def transformar_minutos_em_horas(tempo: int) -> int:
    diferenca_hora = tempo // 60
    diferenca_minuto = tempo % 60
    return diferenca_hora, diferenca_minuto

hora_inicio, minuto_inicio, hora_fim, minuto_fim = input().split()

hora_inicio = int(hora_inicio)
minuto_inicio = int(minuto_inicio)
hora_fim = int(hora_fim)
minuto_fim = int(minuto_fim)

hora_jogada = 0
minuto_jogado = 0

tempo_inicio = transformar_tempo_em_minutos(hora_inicio, minuto_inicio)
tempo_final = transformar_tempo_em_minutos(hora_fim, minuto_fim)

if (hora_inicio == hora_fim) and (minuto_inicio == minuto_fim):
    hora_diferenca = 24
    minuto_diferenca = 0
else:
    if (tempo_final - tempo_inicio) >= 0:
        diferenca_tempo = tempo_final - tempo_inicio
    elif (tempo_final - tempo_inicio) < 0:
        diferenca_tempo = (transformar_tempo_em_minutos(24, 0)) - tempo_inicio
        diferenca_tempo += tempo_final
    hora_diferenca, minuto_diferenca = transformar_minutos_em_horas(diferenca_tempo)

print(f"O JOGO DUROU {hora_diferenca} HORA(S) E {minuto_diferenca} MINUTO(S)")




# if (hora_inicio > hora_fim):
#     hora_jogada = 24 - hora_inicio
#     hora_jogada += hora_fim

#     if (minuto_inicio > minuto_fim):
#         minuto_jogado = 60 - minuto_inicio
#         minuto_jogado += minuto_fim
#     if (minuto_fim > minuto_inicio):
#         minuto_jogado = minuto_fim - minuto_inicio
# elif (hora_inicio == hora_fim) and (minuto_inicio == minuto_fim):
#     hora_jogada = 24
#     minuto_jogado = 0
# else:
#     tempo_jogado = fim - inicio