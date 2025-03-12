# Faça um porgrama que leia algo pelo teclado e mostre a tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(palavra)}.')
print(f'Só tem espaço? {palavra.isspace()}.')
print(f'É numerico? {palavra.isnumeric()}.')
print(f'É alfabetico? {palavra.isalpha()}.')
print(f'É alfanumerico? {palavra.isalnum()}.')
print(f'Está em maisuculas? {palavra.isupper()}.')
print(f'Está em minusculas? {palavra.islower()}.')
print(f'Está capitalizada? {palavra.istitle()}.')






