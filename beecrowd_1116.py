qtde = int(input())

for i in range(qtde):
    num1, num2 = input().split()

    num1 = int(num1)
    num2 = int(num2)

    if num2 == 0:
        print("divisao impossivel")
    else:
        resultado_divisao = num1 / num2
        print(f"{resultado_divisao:.1f}")