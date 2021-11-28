totcom = totmil = cont = menor = 0
barato = ' '
print(f'{"<<<<<Estatísticas De Produtos<<<<<":^50}\n')
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço dos produto: '))
    cont += 1
    totcom += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if opcao == 'N':
        break
print('{:-^40}'.format(' FIM DE PROGRAMA '))
print(f'O total gasto nas compras foi R${totcom}.')
print(f'{totmil} produto custa mais de R$1000.')
print(f'O produto mais barato foi {barato}.')
