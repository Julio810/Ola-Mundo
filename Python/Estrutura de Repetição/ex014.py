pares = 0
impares = 0
for c in range(1, 10):
  if int(input('Digite um número: ')) % 2 == 0:
    pares += 1
  else:
    impares += 1
print(f'Pares: {pares}\n Ímpares: {impares}')