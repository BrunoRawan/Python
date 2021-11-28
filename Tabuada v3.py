print(f'{">>>>Tabuada v3<<<<":^50}')
n = 0
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num <= -1:
        print(f'{"...FIM DE PROGRAMA...":^50}')
        break
    while n < 10:
        n += 1
        result = n * num
        print(f'{num}x{n}={result}')
