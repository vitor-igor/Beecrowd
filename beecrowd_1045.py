lista_numeros = list(input().split())

for i in range(len(lista_numeros)):
    lista_numeros[i] = float(lista_numeros[i])

lista_numeros.sort(reverse=True)

num1 = lista_numeros[0]
num2 = lista_numeros[1]
num3 = lista_numeros[2]

if ((num2 + num3) <= num1):
    print("NAO FORMA TRIANGULO")
elif (num1 ** 2) == ((num2 ** 2) + (num3 ** 2)):
    print("TRIANGULO RETANGULO")
elif (num1 ** 2) > ((num2 ** 2) + (num3 ** 2)):
    print("TRIANGULO OBTUSANGULO")
elif (num1 ** 2) < ((num2 ** 2) + (num3 ** 2)):
    print("TRIANGULO ACUTANGULO")

if num1 == num2 and num2 == num3:
    print("TRIANGULO EQUILATERO")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("TRIANGULO ISOSCELES")