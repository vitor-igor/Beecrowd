qtde_jogadores = int(input())

qtde_saques = 0
qtde_bloqueios = 0
qtde_ataques = 0

qtde_saques_acertados = 0
qtde_bloqueios_acertados = 0
qtde_ataques_acertados = 0

for i in range(qtde_jogadores):
    jogador = input()
    saques, bloqueios, ataques = [int(x) for x in input().split()]
    saques_acertados, bloqueios_acertados, ataques_acertados = [int(x) for x in input().split()]

    qtde_saques += saques; qtde_saques_acertados += saques_acertados
    qtde_bloqueios += bloqueios; qtde_bloqueios_acertados += bloqueios_acertados
    qtde_ataques += ataques; qtde_ataques_acertados += ataques_acertados

porcentagem_saques = (qtde_saques_acertados * 100) / qtde_saques
porcentagem_bloqueios = (qtde_bloqueios_acertados * 100) / qtde_bloqueios
porcentagem_ataques = (qtde_ataques_acertados * 100) / qtde_ataques


print(f"Pontos de Saque: {porcentagem_saques:.2f} %.")
print(f"Pontos de Bloqueio: {porcentagem_bloqueios:.2f} %.")
print(f"Pontos de Ataque: {porcentagem_ataques:.2f} %.")