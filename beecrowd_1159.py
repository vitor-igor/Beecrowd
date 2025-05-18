while True:
    soma = 0
    qtde = 5

    num = int(input())

    if num == 0:
        break
    else:
        while qtde != 0:
            if (num % 2) == 0:
                soma += num
                qtde -= 1
            num += 1
        print(soma)