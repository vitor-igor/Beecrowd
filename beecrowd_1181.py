matriz = []

indice_linha = int(input())

operacao = input()

soma = 0
media = 0

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

for i in range(12):
    soma += matriz[indice_linha][i]

if operacao == "S":
    print(f"{soma:.1f}")
elif operacao == "M":
    media = soma / 12
    print(f"{media:.1f}")