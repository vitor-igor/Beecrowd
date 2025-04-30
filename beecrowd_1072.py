qtde = int(input())

numeros_dentro_do_intervalo = 0
numeros_fora_do_intervalo = 0

for i in range(qtde):
    numero = int(input())
    if numero >= 10 and numero <= 20:
        numeros_dentro_do_intervalo += 1
    else:
        numeros_fora_do_intervalo += 1

print(f"{numeros_dentro_do_intervalo} in")
print(f"{numeros_fora_do_intervalo} out")