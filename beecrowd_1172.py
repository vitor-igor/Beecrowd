vetor = []

for i in range(10):
    num = int(input())

    if num <= 0:
        num = 1
    
    vetor.append(num)
    print(f"X[{i}] = {num}")