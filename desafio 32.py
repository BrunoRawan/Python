from datetime import date
print('Digite 0 caso queira ver se o ano atual é bissexto!')
ano = int(input('Digite um o ano que deseja saber se é bissexto: '))
if ano == 0:# Se (if) o ano for igual a (0)
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))

