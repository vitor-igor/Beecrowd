qtde = int(input())

for i in range(qtde):
    num1, num2 = [int(i) for i in input().split()]

    soma = 0

    if num1 > num2:
        for i in range((num2 + 1), num1):
            if ((i % 2) != 0):
                soma += i
    elif num2 > num1:
        for i in range((num1 + 1), num2):
            if ((i % 2) != 0):
                soma += i

    print(soma)