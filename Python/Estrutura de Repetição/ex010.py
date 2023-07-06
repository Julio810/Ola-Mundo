num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
cont = 0
if num1 > num2:
  for c in range(num2, num1, 1):
    print(c)
    cont += c
else:
  for c in range(num1, num2, 1):
    print(c)
    cont += c
print(f'A soma dos números é: {cont}')