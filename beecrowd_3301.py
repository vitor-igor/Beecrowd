huguinho, zezinho, luisinho = input().split()

huguinho = int(huguinho)
zezinho = int(zezinho)
luisinho = int(luisinho)

if (huguinho > zezinho and huguinho < luisinho) or (huguinho < zezinho and huguinho > luisinho):
    print("huguinho")
elif (zezinho > huguinho and zezinho < luisinho) or (zezinho < huguinho and zezinho > luisinho):
    print("zezinho")
elif (luisinho > huguinho and luisinho < zezinho) or (luisinho < huguinho and luisinho > zezinho):
    print("luisinho")