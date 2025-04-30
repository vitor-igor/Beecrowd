senha_correta = 2002

senha = int(input())
while (senha != senha_correta):
    print("Senha Invalida")
    senha = int(input())

if (senha == senha_correta):
    print("Acesso Permitido")