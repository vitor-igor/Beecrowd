posicao = int(input())

if posicao == 1:
    top = 1
elif posicao <= 3:
    top = 3
elif posicao <= 5:
    top = 5
elif posicao <= 10:
    top = 10
elif posicao <= 25:
    top = 25
elif posicao <= 50:
    top = 50
elif posicao <= 100:
    top = 100

print("Top", top)