a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
delta = (b ** 2) - 4 * a * c
if a == 0:
  print('NÃO É UMA EQUAÇÃO DO SEGUNDO GRAU')
elif delta < 0:
  print('A EQUAÇÃO NÃO POSSUI RAÍZES REAIS')
elif delta == 0:
  print('A EQUAÇÃO POSSUI APENAS UMA RAIZ')
elif delta > 0:
  print('A EQUAÇÃO POSSUI DUAS RAÍZES')