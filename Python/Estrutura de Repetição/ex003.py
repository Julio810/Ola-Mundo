while True:
  nome = str(input('Digite o seu nome: '))
  while not nome:
    if len(nome) < 3:
      print('Dados inválidos')
      nome = str(input('Digite o seu nome: '))
    else:
      print('Valida NOME')
  idade = int(input('Informe a sua idade: '))
  if idade <= 150:
    print('A sua idade está foi VALIDADA')
  else:
    print('A sua idade não foi VALIDADA')
  sexo = ' '
  civil = ' '
  salario = float(input('Qual é o seu salário R$: '))
  if salario < 0:
    print('O seu salário é MENOR que ZERO!')
  else:
    print('O seu salário é MAIOR que ZERO!')
  while sexo not in 'MF':
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
  while civil not in 'SCVD':
    civil = str(input('Informe qual é o seu ESTADO CIVIL: ')).strip().upper()[0]
    if civil == 'S':
      print('Você é SOLTEIRO')
    elif civil == 'C':
      print('Você é CASADO')
    elif civil == 'V':
      print('Você é VIÚVO')
    elif civil == 'D':
      print('Você é DIVORCIADO')
  break

