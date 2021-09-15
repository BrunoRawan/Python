distancia = float(input('Digite a distancia da viagem em km: '))
print('Você vai viajar {} km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da sua passagem vai fica {:.2f}$.'.format(preco))
else:
    preco = distancia * 0.45
    print('Sua passagem vai ficar {:.2f}$.'.format(preco))
print('                             TENHA UMA BOA VIAGEM.....')