from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra.
[ 1 ] Papel.
[ 2 ] Tesoura.''')
jogador = int(input('Digite o número de 0 a 2 para jogar: '))
print('-=' * 30)
print('JO')
sleep(1)
print('KE')
sleep(1)
print('PÔ')
sleep(1)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:  # Computador jogou Pedra.
    if jogador == 0:
        print('EMPATOU...')
    elif jogador == 1:
        print('JOGADOR GANHOU...')
    elif jogador == 2:
        print('COMPUTADOR GANHOU...')
    else:
        print('OPÇÃO INVÁLIDA....')

elif computador == 1:  # Computador jogou Papel.
    if jogador == 0:
        print('COMPUTADOR GANHOU...')
    elif jogador == 1:
        print('EMPATOU...')
    elif jogador == 2:
        print('JOGADOR GANHOU...')
    else:
        print('OPÇÃO INVÁLIDA....')
elif computador == 2:  # computador jogou Tesoura.
    if jogador == 0:
        print('JOGADOR GANHOU...')
    elif jogador == 1:
        print('COMPUTADOR GANHOU...')
    elif jogador == 2:
        print('EMPATOU...')
    else:
        print('OPÇÃO INVÁLIDA....')
