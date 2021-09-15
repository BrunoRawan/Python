from random import choice
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 =  input('Digite o nome do tercceir aluno ')
lista = [n1, n2, n3]
escolhido = choice(lista)
print('O escolhido foi o aluno {}.'.format(escolhido))


