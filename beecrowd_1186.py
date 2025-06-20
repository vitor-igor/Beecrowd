operacao = input()

matriz = []

soma = 0
qtde_elementos = 0
media = 0

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

for linha in range(1, 12):
    for coluna in range(12 - linha, 12):
        soma += matriz[linha][coluna]
        qtde_elementos += 1

media = soma / qtde_elementos

if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{media:.1f}")