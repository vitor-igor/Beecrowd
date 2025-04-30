num = int(input())
horas = num // 60 ** 2
num = num-horas * 60 ** 2

minutos = num // 60
num = num-minutos * 60
seg = num

print(f"{horas}:{minutos}:{seg}")