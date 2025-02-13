nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar not in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

