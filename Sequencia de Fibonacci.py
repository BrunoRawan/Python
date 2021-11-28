print(f'{"Sequência de Fibonacci":-^50}')
n = int(input('Digite um termo: '))
t1 = 0  # Declarando o primeiro termo que eu sei que é 0
t2 = 1  # Declarando o segundo termo que eu sei que é 1
print(f'{t1} → {t2}', end='')  # Mostrando o termo 1 e 2
cont = 3  # Váriavel contador que começa de 3
while cont <= n:  # Emquanto o contador menor que o número digitado pelo o usuário
    t3 = t1 + t2  # O termo 3 vai ser a soma do 1 e 2
    print(f' → {t3} ', end='')
    t1 = t2  # O termo 1 vai passar a ser o 2
    t2 = t3  # E o termo 2 vai passar a ser o 3
    cont += 1  # O contador vai contar de 1 em 1
print('>>>FIM<<<')
