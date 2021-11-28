resposta = 'S'
media = soma = menor = maior = quant = 0
while resposta in 'Ss':# Enquanto o usúario digitar Ss vai repetir o bloco de instrução do while!
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar [S/N]?  ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} e a média foi {media}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
