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

def gerar_cpf(cpf: str) -> str:
    cpf += calcular_digito_b1(cpf)
    cpf += calcular_digito_b2(cpf[:10])

    return cpf
    
###

import sys

entrada = sys.stdin.read().splitlines()

for cpf in entrada:
    cpf_formatado = gerar_cpf(cpf)

    cpf_formatado = f"{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:]}"

    print(cpf_formatado)