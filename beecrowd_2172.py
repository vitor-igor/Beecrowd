while True:
    multiplicador, xp = [int(x) for x in input().split()]

    if multiplicador == 0 and xp == 0:
        break
    
    print(multiplicador * xp)