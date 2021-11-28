num = soma = cont = 0
num = int(input('Digite um número qualquer (999 PARA FINALIZAR): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número qualquer (999 PARA FINALIZAR): '))
print(f' Você digitou {cont} números e a soma entre eles foi {soma}.')
