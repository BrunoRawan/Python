from random import randint

print(f'{"======JOGO DE PAR OU ÌMPAR======":^50}')
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    opcao = ' '
    result = computador + jogador
    while opcao not in "PI":
        opcao = str(input('[P/I]? ')).strip().upper()[0]
    print(f'O computador jogou {computador} e você jogou {jogador} total de {result}. ', end="")
    print('PAR' if result % 2 == 0 else 'DEU PAR')
    if opcao == 'P':
        if result % 2 == 0:
            print('Você ganhou...')
            v += 1
        else:
            print('Você perdeu...')
            break
    elif opcao == 'I':
        if result % 2 == 1:
            print('Você venceu...')
            v += 1
        else:
            print('Você perdeu...')
            break
    print('Vamos jogar de novo... ')
print(f'Você venceu {v} vezes.')
