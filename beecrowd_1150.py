num1 = int(input())
num2 = int(input())

num3 = num1
contador = 1

while not(num2 > num1):
    num2 = int(input())

while not(num3 > num2):
    num1 += 1
    num3 += num1
    contador += 1

print(contador)