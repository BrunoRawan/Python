from math import radians, cos, sin, tan
an = float(input('Digite um ângulo desejado: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O seno do ângulo {} é {:.2f}!'.format(an, seno))
print('O conseno do ângulo {} é {:.2f}!'.format(an, cosseno))
print('A tangente do ângulo {} é {:.2f}!'.format(an, tangente))






