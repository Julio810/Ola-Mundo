litros = float(input('Informe a quantidade de Litros vendidos: '))
combustivel = str(input('Qual o tipo do Combustível: ')).upper()[0]
preco = 0
if combustivel == 'A':
  preco = litros * 1.9
  if litros <= 20:
    preco -= 1.9 * litros * 0.03
  else:
    preco -= 1.9 * litros * 0.05
elif combustivel == 'G':
  preco = litros * 2.5
  if litros <= 20:
    preco -= 2.5 * litros * 0.04
  else:
    preco -= 2.5 * litros * 0.06
print(f'O preço a pagar é R${preco:.2f}')