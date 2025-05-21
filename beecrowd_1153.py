def fatorial(num: int) -> int:
    resultado = num
    if (num - 1) != 0:
        return fatorial(num - 1) * resultado
    return resultado

num = int(input())
print(fatorial(num))