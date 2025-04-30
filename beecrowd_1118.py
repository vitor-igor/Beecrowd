nota1 = 0
nota2 = 0

novo_calculo = 1

while novo_calculo == 1:
    while True:
        nota1 = float(input())

        if nota1 >= 0 and nota1 <= 10:
            break
        elif nota1 < 0 or nota1 > 10:
            print("nota invalida")

    while True:
        nota2 = float(input())

        if nota2 >= 0 and nota2 <= 10:
            break
        elif nota2 < 0 or nota2 > 10:
            print("nota invalida")

    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")

    nota1, nota2 = 0, 0

    print("novo calculo (1-sim 2-nao)")
    novo_calculo = int(input())

    while (novo_calculo != 1) and (novo_calculo != 2):
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = int(input())