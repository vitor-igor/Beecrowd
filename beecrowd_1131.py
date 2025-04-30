qtde_grenais = 0

vitorias_inter = 0
vitorias_gremio = 0
empates = 0

while True:
    qtde_grenais += 1

    gols_inter, gols_gremio = input().split()

    gols_inter = int(gols_inter)
    gols_gremio = int(gols_gremio)

    print("Novo grenal (1-sim 2-nao)")
    grenal = int(input())

    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_gremio > gols_inter:
        vitorias_gremio += 1
    elif gols_inter == gols_gremio:
        empate += 1
    
    if grenal == 2:
        print(f"{qtde_grenais} grenais")
        print(f"Inter:{vitorias_inter}")
        print(f"Gremio:{vitorias_gremio}")
        print(f"Empates:{empates}")

        if vitorias_inter > vitorias_gremio:
            print("Inter venceu mais")
        elif vitorias_gremio > vitorias_inter:
            print("Gremio venceu mais")
        elif vitorias_inter == vitorias_gremio:
            print("Nao houve vencedor")
        break