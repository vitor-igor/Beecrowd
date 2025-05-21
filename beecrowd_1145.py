num1, num2 = [int(i) for i in input().split()]

lista = []
resultado = ""

for i in range(1, num2 + 1):
    lista.append(str(i))
    if (i % num1) == 0 and not(i == (num2)):
        lista.append("\n")
    elif not(i == (num2)):
        lista.append(" ")

resultado = resultado.join(lista)

print(resultado)