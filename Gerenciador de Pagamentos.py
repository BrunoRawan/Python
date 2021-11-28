print(f'{"LOJAS BRUNO":=^40}')
preco = float(input('Digite o preço das compras: R$'))
print('''Digite a opção desejada:
[ 1 ] á vista dinheiro ou cheque: 10% desconto.
[ 2 ] á vista no cartão: 5% desconto.
[ 3 ] 2x no cartão: preço formal.
[ 4 ] 3x ou mais no cartão: 20% de juros.''')
opcao = int(input('Digite a opção.'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('A compra de R${:.2f} com 10% de desconto é {:.2f}R$.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('A compra de R${:.2f} com 5% de desconto é {:.2f}R$.'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('A compra de R${:.2f} 2x no cartão {:.2f}R$.'.format(preco, parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = total / totparcela
    print('A compra de R${:.2f} acima de 3x com juros ficará {:.2f}R$.'.format(preco, total))
else:
    total = preco
    print('Sua compra vai custar R${:.2f}.'.format(total))
    print('Opção invalida de pagameto!!!')
