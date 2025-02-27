"""
2.3 Manipulação de Arquivos
Crie um arquivo texto chamado notas.txt.
Escreva as notas de 5 alunos no arquivo, uma por linha.
Depois, leia o arquivo e calcule a média das notas.

"""

# Escrever as notas no arquivo notas.txt
with open('notas.txt', 'w') as arquivo:
    for i in range(1, 6):
        nota = input(f'Digite a nota do aluno {i}: ')
        arquivo.write(nota + '\n')

print('Notas salvas com sucesso!')

# Ler as notas do arquivo e calcular a média
with open('notas.txt', 'r') as arquivo:
    notas = arquivo.readlines()

# Convertendo as notas para float e calculando a média
notas = [float(nota.strip()) for nota in notas]
media = sum(notas) / len(notas)

print(f'A média das notas é: {media:.2f}')
