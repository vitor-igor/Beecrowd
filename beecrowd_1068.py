expressao = []
qtde_parenteses = 0
qtde_parenteses_aberto = 0
qtde_parenteses_fechado = 0

while True:
    try:
        expressao_entrada = input()
        for i in expressao_entrada:
            expressao.append(i)
            if i == "(":
                qtde_parenteses_aberto += 1
                qtde_parenteses += 1
            elif i == ")":
                qtde_parenteses_fechado += 1
                qtde_parenteses += 1
        
        if ((qtde_parenteses % 2 != 0) and (qtde_parenteses_aberto != qtde_parenteses_fechado)) or (expressao[0] == ")") or (expressao[len(expressao)-1] == "("):
            print("incorrect")
        else:
            print("correct")
    except:
        break

    expressao.clear()
    qtde_parenteses = 0
    qtde_parenteses_aberto = 0
    qtde_parenteses_fechado = 0