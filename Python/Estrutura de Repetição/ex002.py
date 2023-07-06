usuario = input('Digite o nome de usuário: ')
senha = input('Digite a sua senha: ')
while usuario == senha:
  print('Acesso NEGADO!')
  print('Informe novamente suas informações')
  usuario = input('Digite o nome de usuário: ')
  senha = input('Digite a sua senha: ')
print('FIM')