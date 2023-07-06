for c in range(0, 10):
  nota = float(input('Digite a nota do aluno: '))
  if nota > 10:
    print('Valor inválido, TENTE NOVAMENTE')
  else:
    print('A nota do ALUNO é {}'.format(nota))
  break