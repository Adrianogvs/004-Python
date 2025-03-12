# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

# Exibir a média formatada corretamente
print(f'A média das notas {n1} e {n2} é {int(media) if media.is_integer() else round(media, 2)}.')
