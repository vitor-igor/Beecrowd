def sheldon_vence(escolha_sheldon: str, escolha_raj: str) -> bool:
    if (escolha_sheldon == "tesoura" and escolha_raj == "papel") or (escolha_sheldon == "papel" and escolha_raj == "pedra") or (escolha_sheldon == "pedra" and escolha_raj == "lagarto") or (escolha_sheldon == "lagarto" and escolha_raj == "Spock") or (escolha_sheldon == "Spock" and escolha_raj == "tesoura") or (escolha_sheldon == "tesoura" and escolha_raj == "lagarto") or (escolha_sheldon == "lagarto" and escolha_raj == "papel") or (escolha_sheldon == "papel" and escolha_raj == "Spock") or (escolha_sheldon == "Spock" and escolha_raj == "pedra") or (escolha_sheldon == "pedra" and escolha_raj == "tesoura"):
        return True
    else:
        return False

qtde = int(input())

for i in range(qtde):
    escolha_sheldon, escolha_raj = input().split()

    vitoria_sheldon = sheldon_vence(escolha_sheldon, escolha_raj)

    if escolha_sheldon == escolha_raj:
        print(f"Caso #{i + 1}: De novo!")
    elif vitoria_sheldon:
        print(f"Caso #{i + 1}: Bazinga!")
    else:
        print(f"Caso #{i + 1}: Raj trapaceou!")