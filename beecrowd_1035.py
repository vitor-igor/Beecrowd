num1, num2, num3, num4 = input().split()

num1, num2, num3 , num4 = int(num1), int(num2), int(num3), int(num4)

if (num2 > num3) and (num4 > num1) and (num3 + num4 > num1 + num2) and (num3 > 0) and (num4 > 0) and (num1 % 2 == 0):
    print ("Valores aceitos")
else:
    print ("Valores nao aceitos")