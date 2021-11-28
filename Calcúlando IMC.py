peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('IMC da pessoa é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Olha você está abaixo do peso.')
elif 18.6 <= imc <= 25:
    print('Parabéns você ta no peso ideal.')
elif 25 > imc <= 30:
    print('Você está com obrepeso.')
elif 30 >= imc <= 40:
    print('Se cuide você está com obesidade.')
else:
    print('Você precisa se esmagrecer urgente obesidade Mórbida.')
