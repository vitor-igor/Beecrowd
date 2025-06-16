peso1, comprimento1, peso2, comprimento2 = [int(x) for x in input().split()]

lado1 = peso1 * comprimento1
lado2 = peso2 * comprimento2

if lado1 == lado2:
    print(0)
elif lado1 < lado2:
    print(1)
elif lado1 > lado2:
    print(-1)