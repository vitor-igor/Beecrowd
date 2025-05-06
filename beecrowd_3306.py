# def mdc(num1: int, num2: int) -> int:
#     if num2 > num1:
#         return mdc(num2, num1)
#     maior_numero = num1
#     menor_numero = num2

#     if menor_numero == 0:
#         return maior_numero
    
#     resto_divisao = maior_numero % menor_numero

#     return mdc(menor_numero, resto_divisao)

# tamanho_vetor, qtde_queries = input().split()

# tamanho_vetor = int(tamanho_vetor)
# qtde_queries = int(qtde_queries)

# vetor = [int(num) for num in input().split()]

# elementos_query = []

# for i in range(qtde_queries):
#     try:
#         query = [int(num) for num in input().split()]
#     except:
#         continue
#     elementos_query = []
#     resultado_mdc = 0

#     if query[0] == 1:
#         for i in range(query[1], (query[2] + 1)):
#             vetor[i - 1] += query[3]

#     elif query[0] == 2:
#         if query[1] == query[2]:
#             print(vetor[query[1] - 1])
#         else:
#             for i in range(query[1], (query[2] + 1)):
#                 elementos_query.append(vetor[i - 1])
            
#             for i in range(len(elementos_query)):
#                 try:
#                     num1 = elementos_query[i]
#                     num2 = elementos_query[i + 1]
#                     resultado_mdc = mdc(resultado_mdc, elementos_query[i])
#                 except:
#                     break
            
#             print(resultado_mdc)