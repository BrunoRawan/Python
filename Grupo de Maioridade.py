from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Qual ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{menor}ª pessoas são menor de idade.')
print(f'{maior}ª pessoas são maior de idade.')
