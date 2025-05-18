qtde = int(input())

for i in range(qtde):
    num = int(input())

    soma_divisores = 0

    for j in range(1, num // 2 + 1):
        if (num % j) == 0:
            soma_divisores += j
    
    if soma_divisores != num:
        print(f"{num} nao eh perfeito")
    else:
        print(f"{num} eh perfeito")