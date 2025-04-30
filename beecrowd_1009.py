nome = input()
salario_fixo = float(input())
vendas = float(input())

salario_final = salario_fixo + vendas * 0.15

print(f"TOTAL = R$ {salario_final:.2f}")