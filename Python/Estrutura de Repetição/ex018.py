soma = 0
num1 = int(input('Digite o PRIMEIRO número: '))
num2 = int(input('Digite o SEGUNDO número: '))
num3 = int(input('Digite o TERCEIRO número: '))
while soma == 0:
  soma = num1 + num2 + num3
  if num1 > num2 > num3:
    print('O PRIMEIRO número é o MAIOR!')
    break
  elif num2 > num1 > num3:
    print('O SEGUNDO número é o MAIOR!')
    break
  else:
    print('O TERCEIRO número é o MAIOR!')
    break
print('A soma de todos valores será {}'.format(soma))