nota1 = float(input('Informe a PRIMEIRA nota do aluno: '))
nota2 = float(input('Informe a SEGUNDA nota do aluno: '))
nota3 = float(input('Informe a TERCEIRA nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7 and media <= 9.9:
  print(f'O aluno obteve a média de {media}')
  print('APROVADO')
elif media < 7:
  print(f'O aluno obteve a média de {media}')
  print('REPROVADO')
else:
  print('APROVADO COM DISTINÇÃO')