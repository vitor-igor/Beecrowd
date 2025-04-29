def media_ponderada(n1, n2, n3, n4):
    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)
    return media

nota1, nota2, nota3, nota4 = input().split()

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media_aluno = media_ponderada(nota1, nota2, nota3, nota4)

print(f"Media: {media_aluno:.1f}")

if media_aluno >= 7.0:
    print("Aluno aprovado.")
elif media_aluno < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")

    media_aluno = (media_aluno + nota_exame) / 2

    if media_aluno >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media_aluno:.1f}")
    elif media_aluno < 5.0:
        print("Aluno reprovado.")
        print(f"Media final: {media_aluno:.1f}")