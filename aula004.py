# Tipos de dados numéricos: int e float
# int -> Número inteiro
# O tipo 'int' representa qualquer número inteiro, seja positivo ou negativo.
# Se um número inteiro for declarado sem sinal, ele é considerado positivo por padrão.

# float -> Número decimal (ponto flutuante)
# O tipo 'float' representa números com casas decimais, permitindo maior precisão em cálculos.

# Exemplos de uso:
numero_inteiro = 7  # int
numero_decimal = 3.14  # float
numero_negativo_float = -2.718  # float negativo

print(type(numero_inteiro))  # <class 'int'>
print(type(numero_decimal))  # <class 'float'>
print(type(numero_negativo_float))  # <class 'float'>

"""
Em Python, type() é uma função embutida que retorna o tipo de dado de um valor ou variável.

Exemplo:
print(type(10))  # <class 'int'> (Número inteiro)
print(type(3.14))  # <class 'float'> (Número decimal)
print(type("Hello"))  # <class 'str'> (Texto ou string)
print(type(True))  # <class 'bool'> (Booleano - Verdadeiro ou Falso)

O que cada retorno significa?
<class 'int'> → O valor é um número inteiro.
<class 'float'> → O valor é um número decimal (ponto flutuante).
<class 'str'> → O valor é uma string (sequência de caracteres, texto).
<class 'bool'> → O valor é um booleano (True ou False).
A função type() é útil para verificar o tipo de uma variável antes de manipulá-la.

"""