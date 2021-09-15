salario = float(input('Digite seu sálario para calcular o aumento:$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava {:.2f}$, agora passa a ganhar {:.2f}$.'.format(salario, novo))
