# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Digite um valor em metros: '))

centimetros = valor *  100  
milimetros  = valor * 1000  

print(f'O valor {valor} metros equivale a {centimetros:.0f} centímetros e {milimetros:.0f} milímetros.')
