alturah = float(input('Informe a sua altura se for HOMEM: '))
alturam = float(input('Informe a sua altura se for MULHER: '))
homem = (72.7 * alturah) - 58
mulher = (62.1 * alturam) - 44.7
print('O peso ideal para um Homem será {:.2f}'.format(homem))
print('O peso ideal para uma Mulher será {:.2f}'.format(mulher))