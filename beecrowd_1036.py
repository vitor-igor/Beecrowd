coeficiente_a, coeficiente_b, coeficiente_c = input().split()

coeficiente_a = float(coeficiente_a)
coeficiente_b = float(coeficiente_b)
coeficiente_c = float(coeficiente_c)

delta = (coeficiente_b ** 2) - (4 * coeficiente_a * coeficiente_c)

if delta >= 0:
    try:
        resposta_1 = ((- coeficiente_b) + (delta ** (1/2))) / (2 * coeficiente_a)
        resposta_2 = ((- coeficiente_b) - (delta ** (1/2))) / (2 * coeficiente_a)

        print(f"R1 = {resposta_1:.5f}")
        print(f"R2 = {resposta_2:.5f}")
    except:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")