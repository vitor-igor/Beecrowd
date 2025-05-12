lado = int(input())

qtde_casas = lado ** 2

casas_brancas = 0
casas_pretas = 0

if (qtde_casas % 2) != 0:
    casas_brancas = (qtde_casas // 2) + 1
    casas_pretas = qtde_casas // 2
else:
    casas_brancas = qtde_casas // 2
    casas_pretas = qtde_casas // 2

print(f"{casas_brancas} casas brancas e {casas_pretas} casas pretas")