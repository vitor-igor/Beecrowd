while True:
    num1, num2 = [int(i) for i in input().split()]

    if num1 > num2:
        print("Decrescente")
    elif num2 > num1:
        print("Crescente")
    else:
        break