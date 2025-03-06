
numero = int(input('Digite um numero: -->  '))

print(f'\n{5*"=-="} Uso de For ' f'{5*"=-="}\n')

for i in range(0,11):
    valor = i * numero
    print(f'{numero} X {i:02} = {valor:03}.')

print(f'\n{5*"=-="} Uso de While ' f'{5*"=-="}\n')

i = 0

while i < 11:
    valor = i * numero
    print(f'{numero} X {i:02} = {valor:03}.')
    i += 1
