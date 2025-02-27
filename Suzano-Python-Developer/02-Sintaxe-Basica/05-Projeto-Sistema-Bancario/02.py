"""
1.2 Estruturas de Controle
Crie um programa que:

Peça um número inteiro ao usuário.
Verifique se o número é par ou ímpar.
Se for par, imprima "Número par".
Se for ímpar, imprima "Número ímpar".

"""

numero = int(input('Digite um numero inteiro: '))

if numero % 2 == 0:
    print(f'O {numero} digitado é PAR.')
else:
    print(f'O {numero} digitado é IMPAR.')
