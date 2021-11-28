print('-=' * 20)
print('Analisador de Triâgulos')
print('-=' * 20)
seg1 = float(input('Digite o primeiro seguimento: '))
seg2 = float(input('Digite o segundo seguimento: '))
seg3 = float(input('Digite o terceiro seguimento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os seguimentos digitados a cima podem formar um triângulo!')
    if seg1 == seg2 == seg2 == seg3:
        print('EQUILÁTERO.')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os seguimentos não formam triângulo.')
