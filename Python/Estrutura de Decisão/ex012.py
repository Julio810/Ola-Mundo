nota1 = float(input('Digite a PRIMEIRA nota: '))
nota2 = float(input('Digite a SEGUNDA nota: '))
media = (nota1 + nota2) / 2
if media >= 9 < 10:
  print(f'As notas do Aluno foram {nota1} e {nota2}')
  print(f'A sua média de notas corresponde {media}')
  print('Conceito A')
  print('APROVADO')
elif media >= 7.5 < 9:
  print(f'As notas do Aluno foram {nota1} e {nota2}')
  print(f'A sua média de notas corresponde {media}')
  print('Conceito B')
  print('APROVADO')
elif media >= 6 < 7.5:
  print(f'As notas do Aluno foram {nota1} e {nota2}')
  print(f'A sua média de notas corresponde {media}')
  print('Conceito C')
  print('APROVADO')
elif media >= 4 < 6:
  print(f'As notas do Aluno foram {nota1} e {nota2}')
  print(f'A sua média de notas corresponde {media}')
  print('Conceito D')
  print('REPROVADO')
elif media < 4:
  print(f'As notas do Aluno foram {nota1} e {nota2}')
  print(f'A sua média de notas corresponde {media}')
  print('Conceito E')
  print('REPROVADO')