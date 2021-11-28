num = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
if num > num2:
    print('O primeiro valor é maior. '.format(num))
elif num2 > num:
    print('O segundo valor é maior. '.format(num2))
else:
    print('Os números digitados são iguais.')
