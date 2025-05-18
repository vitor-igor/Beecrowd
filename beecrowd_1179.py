par = []
impar = []

for i in range(15):
    num = int(input())

    if (num % 2) == 0:
        par.append(num)
    else:
        impar.append(num)
    
    if len(par) == 5:
        for j in range(5):
            print(f"par[{j}] = {par[j]}")
        par = []
    if len(impar) == 5:
        for j in range(5):
            print(f"impar[{j}] = {impar[j]}")
        impar = []

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")