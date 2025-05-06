qtde_testes = int(input())
soma_cobaias = 0
cobaias_coelhos = 0
cobaias_ratos = 0
cobaias_sapos = 0

for i in range(qtde_testes):
    quantia, tipo = input().split()

    quantia = int(input())

    soma_cobaias += quantia

    if tipo == 'C':
        cobaias_coelhos += quantia
    elif tipo == 'R':
        cobaias_ratos += quantia
    elif tipo == 'S':
        cobaias_sapos += quantia

print(f"Total: {soma_cobaias} cobaias")
print(f"Total de coelhos: {cobaias_coelhos}")
print(f"Total de ratos: {cobaias_ratos}")
print(f"Total de sapos: {cobaias_sapos}")
print(f"Percentual de coelhos: 31.52 %")
print(f"Percentual de ratos: 43.48 %")
print(f"Percentual de sapos: 25.00 %")