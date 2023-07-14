morango = float(input('Informe a quantidade de morangos em KG: '))
maca = float(input('Informe a quantidade de Maçã em KG: '))
preco = 0
if morango <= 5:
  preco += morango * 2.5
else:
  preco += morango * 2.2
if maca <= 5:
  preco += maca * 2.5
else:
  preco += maca * 1.5

if (morango + maca) > 8 or preco > 25:
  preco -= preco * 10 / 100
print(f'O valor a ser pago e R${preco:.2f}')