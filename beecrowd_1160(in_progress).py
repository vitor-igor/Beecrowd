qtde = int(input())

populacaoA, populacaoB, crescimentoA, crescimentoB = 0,0, 0, 0

for i in range(qtde):
    populacaoA, populacaoB, crescimentoA, crescimentoB = input().split()


    populacaoA, populacaoB = int(populacaoA), int(populacaoB)
    crescimentoA, crescimentoB = float(crescimentoA), float(crescimentoB)

    nova_populacaoA = populacaoA * crescimentoA
    if crescimentoB != 0:
        nova_populacaoB = populacaoB * crescimentoB
    else:
        nova_populacaoB = populacaoB

    print(populacaoA, populacaoB, crescimentoA, crescimentoB)
    for j in range(1, 100):
        nova_populacaoA *= crescimentoA

        if crescimentoB != 0:
            nova_populacaoB *= crescimentoB

        print(nova_populacaoA, nova_populacaoB)
    
        print(f"{j + 1} anos")