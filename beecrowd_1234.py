while True:
  try:
    frase = input().lower()
    nova_frase = ''
    status_anterior = True

    for caractere in frase:
      if caractere == ' ':
        nova_frase += caractere
      elif status_anterior == True:
        nova_frase += caractere.upper()
        status_anterior = False
      else:
        nova_frase += caractere 
        status_anterior = True
    print(nova_frase)
  except:
    break