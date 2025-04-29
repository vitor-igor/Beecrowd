num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

if ((num2 % num1) == 0) or ((num1 % num2) == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")