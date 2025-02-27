"""
2.4 Tratamento de Exceções
Crie um programa que peça um número ao usuário.
O programa deve tentar converter o valor para inteiro.
Caso o usuário digite algo que não seja um número, imprima "Digite um número válido."

"""


try:
    numero = int(input('Informe um número: '))
    print(f'Você digitou o número: {numero}')
except ValueError:
    print('Digite um número válido.')
