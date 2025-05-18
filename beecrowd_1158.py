qtde = int(input())

for i in range(qtde):
    soma = 0

    num, qtde_impares = [int(x) for x in input().split()]

    while qtde_impares != 0:
        if (num % 2) != 0:
            soma += num
            qtde_impares -= 1
        num += 1
    
    print(soma)