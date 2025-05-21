numeros = input().split()

num1 = int(numeros[0])
num2 = int(numeros[len(numeros) - 1])
soma = 0

for i in range(num2):
    soma += num1 + i

print(soma)