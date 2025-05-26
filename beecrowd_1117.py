nota1 = 0
nota2 = 0

validador = True

while validador:
    nota1 = float(input())

    if nota1 >= 0 and nota1 <= 10:
        validador = False
    elif nota1 < 0 or nota1 > 10:
        print("nota invalida")

validador = True

while validador:
    nota2 = float(input())

    if nota2 >= 0 and nota2 <= 10:
        validador = False
    elif nota2 < 0 or nota2 > 10:
        print("nota invalida")

media = (nota1 + nota2) / 2

print(f"media = {media:.2f}")