num = int(input('Digite um número inteiro: '))
print('''Escolha a opção abaixo que deseja ser convertida.
[1] Para Binário.
[2] Para Octal.
[3] Para Hexadeciaml.''')
print('-' * 20)
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print('A coversão de {}, é {}. '.format(num, bin(num)[2:]))
elif opcao == 2:
    print('A coversão de {},  é {}. '.format(num, oct(num)[2:]))
elif opcao == 3:
    print('A coversão de {}, é {}.'.format(num, hex(num)[2:]))
else:
    print('A opção digitada esta inválida.....')

