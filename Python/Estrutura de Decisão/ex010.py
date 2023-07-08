hora = int(input('Informe o valor da sua hora de trabalho: '))
mes = int(input('Informe a quantidade de horas trabalhadas no mês: '))
salarioBruto = hora * mes
sindicato = (salarioBruto) - salarioBruto * 0.03
fgts = (salarioBruto) - salarioBruto * 0.11
salarioLiquido = salarioBruto - (sindicato - fgts)
print('DESCONTO DO IR')
if salarioBruto <= 900:
  print('ISENTO')
elif salarioBruto <= 1500:
  print('DESCONTO DE 5%')
  print(f'{salarioBruto * 0.05 + salarioBruto}')
elif salarioBruto <= 2500:
  print('DESCONTO DE 10%')
  print(f'{salarioBruto * 0.1 + salarioBruto}')
else:
  print('DESCONTO DE 20%')
  print(f'{salarioBruto * 0.2 - salarioBruto }')
print(salarioBruto)
print(fgts)
print(sindicato)