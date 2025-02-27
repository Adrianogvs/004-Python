""""
Parte 2: Intermediário
2.1 Manipulação de Strings
Peça uma frase ao usuário.
Conte quantas vogais existem na frase.
Imprima o número de vogais.

"""

def contar_vogais(frase):
    vogais = 'aeiouAEIOU'  # Considera tanto minúsculas quanto maiúsculas
    contador = 0
    
    for letra in frase:
        if letra in vogais:
            contador += 1
            
    return contador

# Solicita a frase do usuário
frase = input('Informe uma frase: ')

# Chama a função e imprime o resultado
quantidade_vogais = contar_vogais(frase)
print(f'A frase tem {quantidade_vogais} vogais.')
