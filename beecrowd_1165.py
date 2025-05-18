qtde = int(input())

for i in range(qtde):
    num = int(input())

    divisores = []

    for j in range(1, num // 2 + 1):
        if (num % j) == 0:
            divisores.append(j)
    
    if len(divisores) > 1:
        print(f"{num} nao eh primo")
    else:
        print(f"{num} eh primo")