frase = str(input('Escreva uma frase : ')).upper().strip()
print('A frase aparece a letra "A" {} vezes.'.format(frase.count('A')))
print('A letra "A" aparece na posição {}.'.format(frase.find('A') +1))
print('A ultima vez que aparece a letra "A" é na posição {}.'.format(frase.rfind('A') +1))

