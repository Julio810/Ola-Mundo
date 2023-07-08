salario = float(input('Informe qual o seu salário atual R$: '))
if salario < 280:
  print(f'O salário atual é R${salario}')
  print('O percentual aplicado para o salário corresponde à 20%')
  print(f'O valor do aumento salarial será R${salario * 0.2}')
  print(f'O seu salário com o resjuste será R${salario * 0.2 + salario}')
elif salario >= 280 and salario < 700:
  print(f'O salário atual é R${salario}')
  print('O percentual aplicado para o salário corresponde à 15%')
  print(f'O valor do aumento salarial será R${salario * 0.15}')
  print(f'O seu salário com o reajuste corresponderá R${salario * 0.15 + salario}')
elif salario >= 700 and salario < 1500:
  print(f'O salário atual é R${salario}')
  print('O percentual aplicado para o salário corresponde à 10%')
  print(f'O valor do aumento salarial será R${salario * 0.1}')
  print(f'O salário com o reajuste corresponderá R${salario * 0.1 + salario}')
else:
  print(f'O salário atual é R${salario}')
  print('O percentual aplicado para o salário corresponde à 5%')
  print(f'O valor do aumento salarial será R${salario * 0.05}')
  print(f'O salário com o reajuste corresponderá R${salario * 0.05 + salario}')