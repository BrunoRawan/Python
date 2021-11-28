from time import sleep

print(f'{"Tabuada 2.0":=^40}')
usuario = int(input('Digite um número de 1 a 9  para ver sua tabuada: '))
print('Aguarde.', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print('.')
sleep(1)
for c in range(1, 10):
    mult = usuario * c
    print('{} x {} = {} '.format(usuario, c, mult))
