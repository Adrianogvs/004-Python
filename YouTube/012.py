"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

# Solicita o preço e faz a conversão correta
produto = float(input("Informe o preço do produto: R$ ").replace(",", "."))

# Calcula o preço com 5% de desconto
desconto = produto * 0.95  

# Exibe o resultado formatado
print(f"O preço do produto com 5% de desconto é de R$ {desconto:.2f}.")
