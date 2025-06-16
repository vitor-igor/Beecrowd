tipo_cha = int(input())
respostas = [int(x) for x in input().split()]

acertos = respostas.count(tipo_cha)

print(acertos)