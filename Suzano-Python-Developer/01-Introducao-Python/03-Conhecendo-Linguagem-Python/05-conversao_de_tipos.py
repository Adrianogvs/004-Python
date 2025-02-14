"""
Conversão de Tipos em Python

Python permite converter tipos de dados utilizando funções como:
- int(): converte para inteiro
- float(): converte para ponto flutuante
- str(): converte para string
- bool(): converte para booleano
"""

# Exemplos de conversão de tipos
a = "10"
b = "20.5"
c = "True"

# Convertendo strings para números
num_inteiro = int(a)
num_flutuante = float(b)
valor_booleano = bool(c)

# Exibir os valores convertidos
print("Número inteiro:", num_inteiro)
print("Número flutuante:", num_flutuante)
print("Valor booleano:", valor_booleano)

# Convertendo de número para string
numero = 42
texto_numero = str(numero)
print("Número como string:", texto_numero)
