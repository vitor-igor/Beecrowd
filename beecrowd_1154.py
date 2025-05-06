soma_idades = 0
qtde_idades = 0

while True:
    idade = int(input())

    if idade > 0:
        soma_idades += idade
        qtde_idades += 1
    else:
        break

media_idade = soma_idades / qtde_idades

print(f"{media_idade:.2f}")