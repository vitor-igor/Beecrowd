def transformar_tempo_em_segundos(hora: int, minuto: int, segundo: int) -> int:
    return (hora * 3600 + minuto * 60 + segundo)

def transformar_segundos_em_horas(tempo: int) -> int:
    diferenca_hora = tempo // 3600
    diferenca_minuto = tempo % 3600 // 60
    diferenca_segundo = tempo % 3600 % 60
    return diferenca_hora, diferenca_minuto, diferenca_segundo

texto, dia = input().split()
hora, minuto, segundo = input().split(" : ")
dia_inicio = int(dia)
hora_inicio = int(hora)
minuto_inicio = int(minuto)
segundo_inicio = int(segundo)

tempo_inicio = transformar_tempo_em_segundos(hora_inicio, minuto_inicio, segundo_inicio)

texto, dia = input().split()
hora, minuto, segundo = input().split(" : ")
dia_final = int(dia)
hora_final = int(hora)
minuto_final = int(minuto)
segundo_final = int(segundo)

tempo_final = transformar_tempo_em_segundos(hora_final, minuto_final, segundo_final)

if (tempo_final - tempo_inicio) >= 0:
    diferenca_tempo = tempo_final - tempo_inicio
    dia_diferenca = dia_final - dia_inicio
elif (tempo_final - tempo_inicio) < 0:
    diferenca_tempo = (transformar_tempo_em_segundos(24, 0, 0)) - tempo_inicio
    diferenca_tempo += tempo_final
    dia_diferenca = dia_final - dia_inicio - 1

hora_diferenca, minuto_diferenca, segundo_diferenca = transformar_segundos_em_horas(diferenca_tempo)

print(f"{dia_diferenca} dia(s)")
print(f"{hora_diferenca} hora(s)")
print(f"{minuto_diferenca} minuto(s)")
print(f"{segundo_diferenca} segundo(s)")