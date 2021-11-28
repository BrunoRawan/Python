n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        result = n1 + n2
        print(f'A soma entre {n1} + {n2} é {result}.')
    elif opcao == 2:
        result = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é {result}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2} o maior número é >>>{maior}.')
        else:
            maior = n2
            print(f'Entre {n1} e {n2} o maior número é >>>{maior}.')
    elif opcao == 4:
        print('INFORME OS NÚMEROS NOVAMENTE.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('>>>FIM DO PROGRAMA<<<')
    else:
        print(f'OPÇÃO INVALIDA.....')
