num = [int(i) for i in input().split()]
lista = num.copy()
num.sort()

print(*num, sep = "\n")
print()
print(*lista, sep = "\n")