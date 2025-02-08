# Definição de strings
texto1 = "Olá, mundo!"  # String com aspas duplas
texto2 = 'Python é incrível!'  # String com aspas simples

# Concatenando strings
frase = "Python" + " " + "é poderoso!"
print(frase)  # Saída: Python é poderoso!

# Acessando caracteres (indexação)
palavra = "Python"
print(palavra[0])  # Saída: P  (primeira letra)
print(palavra[-1])  # Saída: n (última letra)

# Tamanho da string
print(len(palavra))  # Saída: 6 (número de caracteres)

# Convertendo número para string
numero = 42
texto = str(numero)
print(texto)  # Saída: '42'
print(type(texto))  # Saída: <class 'str'>
