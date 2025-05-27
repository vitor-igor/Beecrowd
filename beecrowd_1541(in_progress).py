while True:
    try:
        medidaA, medidaB, percentual = [int(i) for i in input().split()]
    except ValueError:
        break

    area_casa = medidaA * medidaB

    lado_casa = round(area_casa ** (1/2))

    print((lado_casa * 100) // percentual)