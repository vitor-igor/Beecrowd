frase = input()

nova_frase = []

for i in frase:
    if i == ",":
        nova_frase.append("\n")
    else:
        nova_frase.append(i)

print("".join(nova_frase))