num1 = int(input('Digite o PRIMEIRO número: '))
num2 = int(input('Digite o SEGUNDO número: '))
num3 = int(input('Digite o TERCEIRO número: '))
if num1 > num2 > num3:
  print(f'O {num1} é o maior')
elif num2 > num1 > num3:
  print(f'O {num2} número é o maior')
else:
  print(f'O {num3} número é o maior')
menor = num1
if (num2 < menor):
  menor = num2
if (num3 < menor):
  menor = num3
print('Menor:', menor)