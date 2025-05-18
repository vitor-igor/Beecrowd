tamanho_numeros = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6
}

qtde = int(input())

for i in range(qtde):
    qtde_leds = 0
    painel = input()

    for j in painel:
        qtde_leds += tamanho_numeros.get(j)
    
    print(f"{qtde_leds} leds")