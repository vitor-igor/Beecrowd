vetor = []
vetor.append(int(input()))
print(f"N[{0}] = {vetor[0]}")

for i in range(1, 10):
    num = vetor[i - 1] * 2
    vetor.append(num)

    print(f"N[{i}] = {num}")