cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma entre os números digitados foram {soma}.')
print(f'Você digitou {cont} números.')
print(f'{"FIM DE PROGRAMA":-^40}')
