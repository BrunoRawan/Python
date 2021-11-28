nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média entre {:.1f} e {:.1f} é {:.1f}.'.format(nota1, nota2, media))
if media >= 7.0:
    print('Aluno Aprovado...')
if media == 10.0:
    print('Parabéns você tirou a nota máxima!!!')
elif 5.0 <= media < 7:
    print('Aluno de Recuperação...')
else:
    print('Aluno Reprovado...')
