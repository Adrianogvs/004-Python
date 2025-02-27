""""
1.3 Listas e Dicionários
Crie uma lista com 5 números inteiros.
Imprima o maior e o menor número da lista.
Crie um dicionário com os nomes de 3 frutas como chave e o preço como valor.
Imprima o nome da fruta mais cara.

"""

lista = [1, 2, 3, 4, 5]
print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')

frutas = {"uva": 9.90, "abacate": 5.80, "pera": 5.70}
fruta_mais_cara = max(frutas, key=frutas.get)
print(f'A fruta mais cara é: {fruta_mais_cara}')
