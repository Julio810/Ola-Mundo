a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))
if a > (b + c) or b > (c + a) or c > (a + b):
  print('NÃO PODE FORMAR UM TRIÂNGULO')
elif a == b == c:
    print('EQUILÁTERO')
elif a == b or a == c or b == c:
  print('ISÓSCELES')
else:
  print('ESCALENO')