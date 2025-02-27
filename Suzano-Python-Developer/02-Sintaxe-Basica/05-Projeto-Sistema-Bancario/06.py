"""
2.2 Compreensão de Listas
Dado a lista de números:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Crie uma nova lista contendo apenas os números pares usando compreensão de listas.
Crie outra lista contendo o quadrado de cada número ímpar.

"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com números pares usando compreensão de listas
pares = [num for num in numeros if num % 2 == 0]

# Lista com o quadrado dos números ímpares usando compreensão de listas
quadrado_impares = [num**2 for num in numeros if num % 2 != 0]

print(f'Números pares: {pares}')
print(f'Quadrado dos números ímpares: {quadrado_impares}')
