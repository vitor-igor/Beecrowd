coluna = int(input())

operacao = input()

soma = 0

for i in range(12):
    for j in range(12):
        valor = float(input())

        if j == coluna:
            soma += valor

if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    print(f"{(soma / 12):.1f}")