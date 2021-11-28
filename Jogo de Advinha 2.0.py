from random import randint
computador = randint(0, 10)
print('Vou pensar em um número entre 0 e 10 seu objetivo é tentar acertar.')
print('Pensado.....')
acertou = False
pal = 0
while not acertou:
    computador = randint(0, 10)
    jogador = int(input('Em qual número você pensou? '))
    pal += 1
    if jogador == computador:
        print(f'O comutador pensou em {computador}.\n')
        print('Você ganhou Parabéns S2...\n')
        acertou = True
    else:
        print('Você errou tente de novo...')
        if computador > jogador:
            print('Mais')
        elif computador < jogador:
            print('Menos')
print(f'O números de tentativas \033[1;31m{pal}.')
