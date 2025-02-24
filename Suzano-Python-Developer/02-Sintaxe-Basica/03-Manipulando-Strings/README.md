# String e Fatiamento

## Objetivo Geral
Conhecer métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis e entender como funciona o fatiamento.

## Pré-requisitos
- Python 3
- VSCode

## Percurso
- Etapa 1: Conhecendo métodos úteis da classe string
- Etapa 2: Interpolação de variáveis
- Etapa 3: Fatiamento de string
- Etapa 4: String múltiplas linhas

## Etapa 1: Conhecendo métodos úteis da classe string
A classe `str` do Python é rica em métodos que facilitam a manipulação de sequências de caracteres.

### Exemplos de Métodos Úteis
```python
# Maiúscula, Minúscula e Título
texto = "python é incrível"
print(texto.upper())  # PYTHON É INCRÍVEL
print(texto.lower())  # python é incrível
print(texto.title()) # Python É Incrível

# Eliminando espaços em branco
espacos = "   Olá Mundo!   "
print(espacos.strip())   # Olá Mundo!
print(espacos.lstrip())  # 'Olá Mundo!   '
print(espacos.rstrip())  # '   Olá Mundo!'

# Junções e Centralização
nomes = ["Ana", "Bruno", "Carlos"]
print(" - ".join(nomes))  # Ana - Bruno - Carlos
print("Python".center(20, "*"))  # *****Python*****
```

## Etapa 2: Interpolação de variáveis
Em Python, existem 3 formas de interpolar variáveis em strings, mas as duas mais recomendadas são `format()` e `f-strings`.

### Exemplos de Interpolação
```python
# Usando format()
nome = "João"
idade = 25
print("{} tem {} anos".format(nome, idade))  # João tem 25 anos

# Usando f-string (recomendado)
print(f"{nome} tem {idade} anos")  # João tem 25 anos
```

## Etapa 3: Fatiamento de string
Fatiamento de strings é uma técnica utilizada para retornar substrings informando início (`start`), fim (`stop`) e passo (`step`).

### Exemplos de Fatiamento
```python
frase = "Python é incrível"
print(frase[0:6])    # Python
print(frase[7:])     # é incrível
print(frase[:6])     # Python
print(frase[-9:])    # incrível
print(frase[::2])    # Pto énrzl
```

## Etapa 4: String múltiplas linhas
Strings de múltiplas linhas são definidas utilizando 3 aspas simples ou duplas e podem ocupar várias linhas do código.

### Exemplos de Strings Múltiplas Linhas
```python
texto = '''
Esse é um exemplo de
string com múltiplas
linhas em Python.
'''
print(texto)
```

