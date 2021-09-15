from time import sleep
from random import randint
computador = randint(0, 5)# FAZ O COMPUTADOR GRAVAR UM NUMERO
print('-'*20)
print('Vou pensar em numero entre 0 e 5 será que você advinha? ')
print('AGUARDE.....')
sleep(5)
print('-'*20)
jogador =  int(input('Em qual número eu pensei? '))# O JOGADOR TENTA ADIVINHAR
print('-'*20)
if jogador == computador:# SE O JOGADOR PENSOU NO MESMO NÚMERO QUE O COMPUTADOR
    print('---------Parabéns Você Ganhou----------- ')
else:
    print('Você perdeu! Eu pensei no número {} e não no {}.'.format(computador, jogador))







