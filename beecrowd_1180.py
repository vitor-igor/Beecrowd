n = int(input())
num = [int(i) for i in input().split()]
print("Menor valor:", min(num))
print("Posicao:", num.index(min(num)))