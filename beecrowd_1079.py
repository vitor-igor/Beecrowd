qtde = int(input())

for i in range(qtde):
    num1, num2, num3 = input().split()

    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)

    media = ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10

    print(f"{media:.1f}")