"""
Variáveis em Python
Variáveis são usadas para armazenar valores em Python. Elas podem armazenar diferentes tipos de dados, como números, strings, listas, etc.

🔹 Criando Variáveis
Para criar uma variável, basta escolher um nome e atribuir um valor a ela usando o operador =.
"""
nome = "Maria"  # String (texto)
idade = 30  # Inteiro
altura = 1.65  # Float (número decimal)
ativo = True  # Booleano (True ou False)


"""
🔹 Regras para nomes de variáveis
✅ Devem começar com uma letra ou underscore (_)
✅ Podem conter letras, números e underscores (_)
✅ Não podem começar com números
✅ Python diferencia maiúsculas e minúsculas (idade ≠ Idade)
✅ Não podem ser palavras reservadas (exemplo: def, class, if, etc.)
"""
# ✅ Exemplos válidos:
nome = "Lucas"
_idade = 28
altura_pessoa = 1.80
preco_total = 99.99

# ❌ Exemplos inválidos:
2nome = "João"  # ❌ Começa com número
nome completo = "Ana"  # ❌ Espaços não são permitidos
class = "Python"  # ❌ 'class' é uma palavra reservada

"""
PEP 8 – Convenções de Estilo para Python
O PEP 8 é um guia de boas práticas para escrever código Python legível e organizado. Ele define padrões para nomeação de variáveis, espaçamento, indentação, etc.

🔹 1. Nomeação de Variáveis
✅ Use nomes descritivos para facilitar a compreensão do código.
✅ Variáveis devem ser minúsculas com underscores (_) entre palavras.
"""
# Correto ✅
nome_completo = "Carlos Silva"
quantidade_produtos = 5

# Errado ❌
NomeCompleto = "Carlos Silva"  # Evite CamelCase em variáveis
qtdPdt = 5  # Nome pouco descritivo


# Correto ✅
def somar(a, b):
    resultado = a + b
    return resultado

# Errado ❌ (mistura de TAB e espaços, além de indentação errada)
def somar(a, b):
	resultado = a + b   # TAB usado ao invés de espaços
	  return resultado  # Indentação errada


"""
Comprimento das Linhas
✅ O limite recomendado é máximo 79 caracteres por linha.
✅ Se precisar quebrar linhas longas, use \ ou parênteses:
"""
# Correto ✅
mensagem = (
    "Este é um exemplo de uma string muito longa "
    "que está sendo dividida corretamente."
)

# Errado ❌ (muito longa)
mensagem = "Este é um exemplo de uma string muito longa que não deve ultrapassar o limite de 79 caracteres"


"""
Espaços em Expressões
✅ Use espaços ao redor dos operadores, mas evite espaços desnecessários.
"""
# Correto ✅
resultado = (10 + 5) * 2

# Errado ❌
resultado=(10+5)*2  # Difícil de ler


"""
Importações
✅ Cada importação deve ser em uma linha separada e organizada.
"""
# Correto ✅
import os
import sys

# Errado ❌ (importação na mesma linha)
import os, sys  
