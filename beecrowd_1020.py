idade_dias = int(input())

idade_ano = idade_dias // 365
idade_mes = (idade_dias % 365) // 30
idade_dias = ((idade_dias % 365) % 30)

print(f"{idade_ano} ano(s)")
print(f"{idade_mes} mes(es)")
print(f"{idade_dias} dia(s)")