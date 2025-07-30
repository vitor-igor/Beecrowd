produtos = {
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5
}

codigo, quantidade = [int(x) for x in input().split()]

total = produtos[codigo] * quantidade

print(f"Total: R$ {total:.2f}")