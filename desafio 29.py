km = float(input('Digite a velocidade do carro: '))
print('.'*50)
if km > 80:
    print('MULTADO! Você ultapassou o limite de 80km/h.')
    print('.'*50)
    multa = (km-80) * 7
    print('Você pagara uma multa de {:.2f}$.'.format(multa))
    print('.'*50)
print('Dirija com segurança!')