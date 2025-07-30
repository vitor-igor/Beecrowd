qtde = int(input())

for i in range(qtde):
    texto = ""
    texto_codificado = input()
    diferenca = int(input())

    for simbolo in texto_codificado:
        if (ord(simbolo) - diferenca) >= 65:
            texto += chr(ord(simbolo) - diferenca)
        else:
            texto += chr((ord(simbolo) + 26 - diferenca))

    print(texto)