
# String e Fatiamento

# Etapa 1: Conhecendo métodos úteis da classe string

# Maiúscula, Minúscula e Título
texto = "python é incrível"
print(texto.upper())  # PYTHON É INCRÍVEL
print(texto.lower())  # python é incrível
print(texto.title())  # Python É Incrível

# Eliminando espaços em branco
espacos = "   Olá Mundo!   "
print(espacos.strip())   # Olá Mundo!
print(espacos.lstrip())  # 'Olá Mundo!   '
print(espacos.rstrip())  # '   Olá Mundo!'

# Junções e Centralização
nomes = ["Ana", "Bruno", "Carlos"]
print(" - ".join(nomes))  # Ana - Bruno - Carlos
print("Python".center(20, "*"))  # *****Python*****

# Etapa 2: Interpolação de variáveis

# Usando format()
nome = "João"
idade = 25
print("{} tem {} anos".format(nome, idade))  # João tem 25 anos

# Usando f-string (recomendado)
print(f"{nome} tem {idade} anos")  # João tem 25 anos

# Etapa 3: Fatiamento de string

frase = "Python é incrível"
print(frase[0:6])    # Python
print(frase[7:])     # é incrível
print(frase[:6])     # Python
print(frase[-9:])    # incrível
print(frase[::2])    # Pto énrzl

# Etapa 4: String múltiplas linhas

texto = '''
Esse é um exemplo de
string com múltiplas
linhas em Python.
'''
print(texto)
