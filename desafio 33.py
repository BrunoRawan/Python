a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a  # estou declarando que o valor1 é o menor
# verificando qual é o menor valor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando qual é o maior valor
maior = a

if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
# Agora vou dizer quem é maior e quem é menor
print('O menor valor digitado foi {}.'.format(menor))
print('E o maior foi {}.'.format(maior))
