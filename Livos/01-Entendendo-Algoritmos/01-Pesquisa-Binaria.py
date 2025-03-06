"""
Aqui está um exemplo de Pesquisa Binária em Python, baseado no que é explicado no livro Entendendo Algoritmos, de Aditya Y. Bhargava:

🔹 O que é a Pesquisa Binária?
    A Pesquisa Binária é um algoritmo eficiente para encontrar um item em uma lista ordenada. 
    Ele funciona dividindo repetidamente a lista ao meio e descartando a metade que não contém o item procurado.
"""

def pesquisa_binaria(lista, item):  # item é passado como argumento
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]  # Pegamos o valor do meio da lista

        if chute == item:  # Comparação com o número que estamos procurando
            return meio  # Encontramos o número e retornamos a posição!
        elif chute > item:
            alto = meio - 1  # Ajustamos a busca para a metade menor
        else:
            baixo = meio + 1  # Ajustamos a busca para a metade maior

    return None  # Retorna None se o número não estiver na lista

# Criamos uma lista ordenada
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]

# Definimos o número que queremos encontrar e chamamos a função
item_procurado = 7  # Esse é o "item" que será passado para a função
resultado = pesquisa_binaria(lista_ordenada, item_procurado)

if resultado is not None:
    print(f"Item encontrado na posição {resultado}")
else:
    print("Item não encontrado")



"""
🔹 Como funciona?
Pegamos uma lista ordenada e um número que queremos encontrar.

Verificamos o elemento do meio:
    1. Se for o item que buscamos, retornamos a posição.
    2. Se for maior, descartamos a metade superior.
    3. Se for menor, descartamos a metade inferior.

Repetimos o processo até encontrar o item ou reduzir a busca a um único elemento.

📌 Complexidade:
Melhor caso:  𝑂(1) O(1) (se o elemento do meio for o item buscado). 
Pior caso e caso médio:  𝑂(log⁡𝑛)O(logn) (reduzimos a busca pela metade a cada iteração).

Esse algoritmo é muito mais rápido que a Busca Linear (𝑂(𝑛)O(n)) para listas grandes. 🚀

"""