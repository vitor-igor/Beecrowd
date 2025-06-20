porcoes = {0: 300, 1: 1500, 2: 600, 3: 1000, 4: 150, "Chica": 225}

mandioca = porcoes["Chica"]

for i in range(5):
    entrada = int(input())

    mandioca += porcoes[i] * entrada

print(mandioca)