while True:
    num = int(input())
    lista = []

    if num == 0:
        break
    else:
        for i in range(1, num + 1):
            if i == num:
                lista.append(str(i))
            else:
                lista.append(f"{i} ")
    
    resultado = "".join(lista)
    print(resultado)