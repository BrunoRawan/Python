print(f'{"Gerador de PA":=^40}')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('>>PAUSA<<')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print(f"Progressão finalizada com {total} mostrados.")
