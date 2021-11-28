casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos quer pagar? '))
prestacao = casa / (anos * 12)
print('Pra pagar uma casa de {:.2f}R$ em {} anos '.format(casa, anos), end='')
print('a prestação será de {:.2f}R$.'.format(prestacao))
minimo = salario * 30 / 100
if prestacao <= minimo:
    print('=-' * 20)
    print('Seu empréstimo foi aprovado com sucesso!!!!')

else:
    print('Empréstimo não aprovado, tente outro dia.')
