salario = float(input('Qual o seu salário por hora trabalhada R$ '))
hora = 220
salarioBruto = salario * 220
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato
print('O salário bruto corresponde: R$ {:.2f}'.format(salarioBruto))
print('O desconto do Imposto de Renda será: R${:.2f}'.format(ir))
print('O desconto do INSS é: R${:.2f}'.format(inss))
print('O imposto sindical corresponde: R${:.2f}'.format(sindicato))
print('O Salário Líquido será: R${:.2f}'.format(salarioLiquido))