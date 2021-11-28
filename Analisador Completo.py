somaidade = 0
mediaidade = 0
maioridadehomem = 0
totmulhe20 = 0
nomevelho = 0
for p in range(1, 5):
    print(f'----------{p}ª pessoa----------')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo [M]/[F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulhe20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade}.')
print(f'O homem mais velho se chama {nomevelho}, e têm {maioridadehomem} anos.')
print(f'Ao todo são {totmulhe20} com menos de 20 anos.')
