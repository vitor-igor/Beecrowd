import sys

def criptografar(texto: str) -> str:
    lista_caracteres = []
    lista = []

    # Primeira Passada
    for caractere in texto:
        if caractere.isalpha():
            lista_caracteres.append(chr(ord(caractere) + 3))
        else:
            lista_caracteres.append(caractere)

    # Segunda Passada    
    lista_caracteres.reverse()

    # Terceira Passada    
    tamanho = len(lista_caracteres)
    for i in range(tamanho // 2):
        lista.append(lista_caracteres[i])
    for i in range(tamanho // 2, tamanho):
        caractere = chr(ord(lista_caracteres[i]) - 1)
        lista.append(caractere)

    resultado = "".join(lista)
    return resultado

qtde_testes = int(input())

for _ in range(qtde_testes):
    texto = input()
    print(criptografar(texto))