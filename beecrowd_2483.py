frase = "Feliz nat"

qtde = int(input())

for i in range(qtde):
    if i == (qtde - 1):
        frase += "al!"
    else:
        frase += "a"

print(frase)