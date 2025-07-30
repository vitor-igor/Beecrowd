combustivel = {
    1: "alcool",
    2: "gasolina",
    3: "diesel",
}

contador = {
    "alcool": 0,
    "gasolina": 0,
    "diesel": 0
}

numero = 0

while True:
    numero = int(input())
    while (numero <= 0) or (numero > 4):
        numero = int(input())
    if (numero == 4):
        break
    else:
        contador[combustivel[numero]] += 1

print("MUITO OBRIGADO")
print(f"Alcool: {contador['alcool']}")
print(f"Gasolina: {contador['gasolina']}")
print(f"Diesel: {contador['diesel']}")