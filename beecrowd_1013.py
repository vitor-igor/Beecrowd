num1, num2, num3 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

maior = 0

if num1 > num2 and num1 > num3:
  maior = num1

elif num2 > num3:
  maior = num2

else:
  maior = num3

print(f"{maior} eh o maior")