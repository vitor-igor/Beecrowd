def calcular_digito_b1(cpf: str) -> str:
    digitos = [int(x) for x in cpf]

    digito = 0

    for i in range(9):
        digito += digitos[i] * (i + 1)

    if (digito % 11) == 10:
        return "0"
    else:
        digito = digito % 11
        return str(digito)

def calcular_digito_b2(cpf: str) -> str:
    digitos = [int(x) for x in cpf]

    digito = 0

    for i in range(9):
        digito += digitos[i] * (9 - i)

    if (digito % 11) == 10:
        return "0"
    else:
        digito = digito % 11
        return str(digito)

def validar_cpf(cpf: str) -> bool:
    if cpf[9] == calcular_digito_b1(cpf) and cpf[10] == calcular_digito_b2(cpf):
        return True
    else:
        return False
    
###

import sys

entrada = sys.stdin.read().splitlines()

for cpf in entrada:
    cpf = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:]

    if validar_cpf(cpf):
        print("CPF valido")
    else:
        print("CPF invalido")