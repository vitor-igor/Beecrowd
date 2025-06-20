qtde = int(input())

total = 0

produtos = {1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005: 5.50}

for i in range(qtde):
    prod, multiplicador = [int(x) for x in input().split()]

    total += produtos[prod] * multiplicador

print(f"{total:.2f}")