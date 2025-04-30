qtde = int(input())

tipo = ''

for i in range(qtde):
    numero = int(input())

    if (numero != 0 and ((numero % 2) == 0)):
        tipo += "EVEN "
    elif (numero != 0 and ((numero % 2) != 0)):
        tipo += "ODD "
    
    if (numero == 0):
        tipo += "NULL"
    else:
        if numero > 0:
            tipo += "POSITIVE"
        elif numero < 0:
            tipo += "NEGATIVE"
    
    print(tipo)
    tipo = ''