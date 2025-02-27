""""
1.4 Funções
Escreva uma função chamada calcular_media que:

Receba uma lista de números.
Retorne a média desses números.
Utilize a função para calcular a média de uma lista fornecida pelo usuário.

"""

def calcular_media(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

# Solicitando a lista de números do usuário
entrada = input('Informe alguns números separados por vírgula: ')
# Convertendo a entrada para uma lista de números
lista = [float(num) for num in entrada.split(',')]

# Chamando a função e imprimindo o resultado
media = calcular_media(lista)
print(f'A média dos números é: {media}')
