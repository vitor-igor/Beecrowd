dias, saldo = [int(x) for x in input().split()]

registro_saldos = []

for i in range(dias):
    entrada = int(input())

    saldo += entrada

    registro_saldos.append(saldo)

print(min(registro_saldos))