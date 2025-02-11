primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if segundo_valor > primeiro_valor:
    print(f'Segundo valor {segundo_valor} é maior que o primeiro {primeiro_valor}.')
elif primeiro_valor > segundo_valor:
    print(f'Primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
else:
    print(f'Os dois valores são iguais.')