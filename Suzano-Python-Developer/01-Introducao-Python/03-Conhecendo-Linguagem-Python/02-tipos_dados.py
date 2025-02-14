# Tipos de Dados em Python

"""
Os tipos built-in são:

| Tipo      | Exemplos                           |
|-----------|------------------------------------|
| Texto     | `str`                              |
| Números   | `int`, `float`, `complex`          |
| Sequência | `list`, `tuple`, `range`           |
| Mapa      | `dict`                             |
| Coleção   | `set`, `frozenset`                 |
| Booleano  | `bool`                             |
| Binário   | `bytes`, `bytearray`, `memoryview` |
|-----------|------------------------------------|

Tipos Númericos

a) Inteiros
   Representados pela class int, exemplo:
   1,10,100, -1, -10, -100, ... 99001823

b) Ponto flutuante
   Represetando pela class float, exemplo:
   1.5, -10.543, 0.76 ... 99999.002

c) Tipos Booleanos:
   Representado pela class bool, exemplo:
   0 = False
   1 = True

d) Tipos Strings:
   Representado pela class str, exemplo:
   "Python", 'Python'

"""
"""
Tipos de Dados em Python

Python possui diversos tipos de dados embutidos, incluindo:
- int (inteiro)
- float (número de ponto flutuante)
- str (string)
- bool (booleano)
- list (lista)
- tuple (tupla)
- dict (dicionário)
- set (conjunto)
"""

# Exemplos de tipos de dados
inteiro = 10
flutuante = 10.5
texto = "Olá, Python!"
booleano = True
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
dicionario = {"nome": "Python", "versao": 3.10}
conjunto = {1, 2, 3, 4, 5}

# Exibir os tipos de cada variável
print(type(inteiro))
print(type(flutuante))
print(type(texto))
print(type(booleano))
print(type(lista))
print(type(tupla))
print(type(dicionario))
print(type(conjunto))
