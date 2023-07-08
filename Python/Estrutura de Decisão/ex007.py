prod1 = float(input('Qual o valor do PRIMEIRO produto R$ '))
prod2 = float(input('Qual o valor do SEGUNDO produto R$ '))
prod3 = float(input('Qual o valor do TERCEIRO produto R$ '))
menor = prod1
if (prod2 < menor):
  menor = prod2
if (prod3 < menor):
  menor = prod3
print(f'O produto a ser comprado é o {menor}')