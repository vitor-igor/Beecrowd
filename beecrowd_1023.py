import sys

entrada = sys.stdin.read().splitlines()
indice = 0
numero_cidade = 1

while True:
    if indice >= len(entrada):
        break

    qtde = int(entrada[indice])
    indice += 1
    if qtde == 0:
        break

    qtde_total_moradores = 0
    consumo_total = 0
    consumo_dict = {}

    for _ in range(qtde):
        qtde_moradores, consumo_imovel = [int(h) for h in entrada[indice].split()]
        indice += 1

        consumo_medio_imovel = consumo_imovel // qtde_moradores

        qtde_total_moradores += qtde_moradores
        consumo_total += consumo_imovel

        if consumo_medio_imovel in consumo_dict:
            consumo_dict[consumo_medio_imovel] += qtde_moradores
        else:
            consumo_dict[consumo_medio_imovel] = qtde_moradores

    lista_consumo_imovel = sorted(consumo_dict.items())
    exibir_lista_consumo_imovel = " ".join(f"{v}-{k}" for k, v in lista_consumo_imovel)

    consumo_medio_geral = int((consumo_total / qtde_total_moradores) * 100) / 100

    if numero_cidade > 1:
        print()
    print(
        f"Cidade# {numero_cidade}:\n"
        f"{exibir_lista_consumo_imovel}\n"
        f"Consumo medio: {consumo_medio_geral:.2f} m3."
    )

    numero_cidade += 1
