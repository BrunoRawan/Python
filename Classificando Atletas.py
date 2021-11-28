from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - ano_nasc
categoria = idade
print('Quem nasceu em {}, têm {} anos.'.format(ano_nasc, idade))
if idade < 10:
    print('Você têm {} anos, e é da categoria MIRIM.'.format(idade))
elif idade < 15:
    print('Você têm {} anos, e é da categoria INFANTIL.'.format(idade))
elif idade < 20:
    print('Você têm {} anos, e é da categoria JÚNIOR.'.format(idade))
elif idade < 26:
    print('Você têm {} anos, e é da categoria SÊNIOR.'.format(idade))
elif idade > 25:
    print('Você têm {} anos, e é da categoria MASTER.'.format(idade))
if ano_nasc == 0:
    print('Nada digitado...')

