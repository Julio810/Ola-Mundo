positivo = 0
resposta = str(input('Telefonou para a vítima? [S / N]: ')).upper()
if resposta == 'S':
  positivo += 1
resposta1 = str(input('Esteve no local do crime? [S / N]: ')).upper()
if resposta1 == 'S':
  positivo += 1
resposta2 = str(input('Mora perto da vítima? [S / N]: ')).upper()
if resposta2 == 'S':
  positivo += 1
resposta3 = str(input('Devia para a vítima? [S / N]: ')).upper()
if resposta3 == 'S':
  positivo += 1
resposta4 = str(input('Já trabalhou com a vítima? [S / N]: ')).upper()
if resposta4 == 'S':
  positivo += 1

if positivo < 2:
  print('INOCENTE')
elif positivo == 2:
  print('SUSPEITA')
elif positivo < 5:
  print('CÚMPLICE')
else:
  print('ASSASSINO')