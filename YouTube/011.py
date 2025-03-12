"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

largura = float(input('Informe a largura em metros: '))
altura = float(input('Informe a altura em metros: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem uma dimensão de {largura} por {altura} e sua área é de {area}m².')
print(f'Para pintar essa parede precisa de {tinta} litros de tinta.')
