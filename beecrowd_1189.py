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

for coluna in range(0, 11 // 2):
    for linha in range(1 + coluna, 11 - coluna):
        soma += matriz[linha][coluna]
        qtde_elementos += 1

media = soma / qtde_elementos

if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{media:.1f}")