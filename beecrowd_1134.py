contador_alcool = 0
contador_gasolina = 0
contador_diesel = 0

numero = 0

while True:
    numero = int(input())
    while (numero <= 0) or (numero > 4):
        numero = int(input())
    if (numero == 4):
        break

    if (numero == 1):
        contador_alcool += 1
    elif (numero == 2):
        contador_gasolina += 1
    elif (numero == 3):
        contador_diesel += 1

print("MUITO OBRIGADO")
print(f"Alcool: {contador_alcool}")
print(f"Gasolina: {contador_gasolina}")
print(f"Diesel: {contador_diesel}")