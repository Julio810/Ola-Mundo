turno = str(input('Qual o TURNO você estuda: ')).upper()[0]
if turno == 'M':
  print('Bom Dia')
elif turno == 'V':
  print('Boa Tarde')
elif turno == 'N':
  print('Boa Noite')
else:
  print('Valor inválido')