area = float(input('Digite o tamanho da área a ser pintada: M² '))
litros = area / 3
latas = int(litros / 18)
if litros % 18 != 0:
  latas += 1
print('Você deverá comprar', latas, 'latas.')
print('O valor total é:', latas * 80)