ddd = int(input())

lista_ddd = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

if bool(lista_ddd.get(ddd)):
    print(lista_ddd.get(ddd))
else:
    print("DDD nao cadastrado")