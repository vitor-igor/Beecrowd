codigo, quantidade = input().split()

quantidade = int(quantidade)

total = 0

if (codigo == "1"):
    total = 4.0 * quantidade
elif (codigo == "2"):
    total = 4.5 * quantidade
elif (codigo == "3"):
    total = 5.0 * quantidade
elif (codigo == "4"):
    total = 2.0 * quantidade
elif (codigo == "5"):
    total = 1.5 * quantidade

print(f"Total: R$ {total:.2f}")