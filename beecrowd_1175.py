vetor = []
inicio_vetor = []
final_vetor = []

for i in range(20):
    num = int(input())
    
    vetor.append(num)

for j in range(10):
    final_vetor.append(vetor[j])
    inicio_vetor.append(vetor[(19 - j)])

final_vetor.reverse()
inicio_vetor.extend(final_vetor)

vetor = inicio_vetor

for x in range(len(vetor)):
    print(f"N[{x}] = {vetor[x]}")