peso = float(input('Informe a quantidade de KG que possui o peixe: '))
excesso = peso - 50
multa = excesso * 4
print('O peso do referido peixe é {}KG'.format(peso))
print('O total do peso excedido foi {}KG'.format(excesso))
print('A multa que João deverá pagar custa {}R$'.format(multa))