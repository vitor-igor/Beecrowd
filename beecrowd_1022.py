qtde = int(input())

simplificador = []

for i in range(qtde):
    expressao = input().split()

    num1 = int(expressao[0])
    num2 = int(expressao[2])

    operador = expressao[3]

    num3 = int(expressao[4])
    num4 = int(expressao[6])

    if operador == "+" or operador == "-":
        denominador = num2 * num4
        valor1_denominador = num1 * num4
        valor2_denominador = num3 * num2 
        if operador == "+":
            numerador = valor1_denominador + valor2_denominador
        else:
            numerador = valor1_denominador - valor2_denominador

    elif operador == "*":
        numerador = num1 * num3
        denominador = num2 * num4
    elif operador == "/":
        numerador = num1 * num4
        denominador = num2 * num3

    if numerador % denominador == 0:
        numero_simplificado = f"{int(numerador / denominador)}/1"
    else:
        for j in range(1, denominador // 2):
            if (numerador % j == 0) and (denominador % j == 0):
                simplificador.append(j)

        numerador_simplificado = int(numerador / simplificador[len(simplificador) - 1])
        denominador_simplificado = int(denominador / simplificador[len(simplificador) - 1])
        if denominador_simplificado == 1:
            numero_simplificado = f"{numerador_simplificado}/1"
        else:
            numero_simplificado = f"{numerador_simplificado}/{denominador_simplificado}"

    print(f"{numerador}/{denominador} = {numero_simplificado}")