num = int(input('Digite um número para verificar se ele é primo: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisivél {}.'.format(num, total))
if total == 2:
    print('È por isso que ele é primo!')
else:
    print('É por isso que ele não é primo!')
    
