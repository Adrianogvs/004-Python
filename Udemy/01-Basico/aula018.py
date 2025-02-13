"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite um nome: ').strip()  # .strip() remove espaços extras
idade = input('Digite sua idade: ').strip()

# Conta os espaços no nome
espaco = len([c for c in nome if c in " "])

# Verifica se nome e idade não estão vazios
if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém {espaco} espaços.')
    print(f'Seu nome tem {len(nome) - espaco} letras.')

    # Apenas imprime a primeira e última letra se nome não estiver vazio
    if len(nome) > 0:
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
