salario = float(input())

salario_nao_isento = 0
taxa = 0

if salario <= 2000.0:
    print("Isento")
else:
    salario_nao_isento = salario - 2000.0

    if salario <= 3000.0:
        taxa = salario_nao_isento * 0.08
    elif salario <= 4500.0:
        taxa = (salario_nao_isento - 1000.0) * 0.18
        taxa += 1000.0 * 0.08
    else:
        taxa = (salario_nao_isento - 2500.0) * 0.28
        taxa += 1500.0 * 0.18
        taxa += 1000.0 * 0.08
    
    print(f"R$ {taxa:.2f}")