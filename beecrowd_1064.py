soma = 0
positivos = 0

for i in range(6):
    numero = float(input())
    if (numero>0):
        positivos = positivos + 1
        soma = soma + numero
        
        
media = soma / positivos
print("{} valores positivos".format(positivos))
print("{:.1f}".format(media))