"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
produto = float(input('Informe o preco do produto: R$'))
ajuste = produto * 1.05
desconto = produto + (produto - ajuste)

print(f'O preco do produto com o ajuste de 5% é de R${desconto:.2f}.')