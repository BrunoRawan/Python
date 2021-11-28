print(f'{"Analise De Dados":=^50}')
mais18 = hcas = mcas20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0:]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        hcas += 1
    if sexo == 'F' and idade < 20:
        mcas20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f"{mais18} pessoas têm mais de 18 anos.")
print(f"Foram cadastrados {hcas} homen(s).")
print(f"{mcas20} mulhere(s) têm menos de 20 anos.")