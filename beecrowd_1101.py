while True:
    num1, num2 = [int(i) for i in input().split()]

    lista_numeros = []
    soma = 0

    if (num1 <= 0) or (num2 <= 0):
        break
    else:
        if num1 > num2:
            for i in range(num2, num1 + 1):
                lista_numeros.append(str(i))
                soma += i
        elif num2 > num1:
            for i in range(num1, num2 + 1):
                lista_numeros.append(str(i))
                soma += i
        
        resultado = " ".join(lista_numeros)

        print(f"{resultado} Sum={soma}")