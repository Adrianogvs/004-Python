"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e x - Hexadecial (ABSCDF0123456789)
.<número de digitos>f
(Caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^- Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

nome = 'Adriano'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

variavel1 = 'ABC'
print(f'{variavel1}')
print(f'{variavel1: >10}.')
print(f'{variavel1: <10}.')
print(f'{variavel1: ^10}.')

"""
O documento foi criado com todas as informações do curso de Python. Se precisar de ajustes ou quiser adicionar mais detalhes, é só avisar! 🚀🐍

# Interpolação de Strings em Python

A interpolação de strings é uma técnica utilizada para inserir valores dentro de uma string formatada. Em Python, existem diversas formas de realizar essa interpolação.

## Tipos de Interpolação

### 1️⃣ Formatação com `%` (estilo C, antigo)
```python
nome = 'Adriano'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
```
🔹 **Saída:**
```
Adriano, o preço é R$1000.96
O hexadecimal de 1500 é 000005DC
```

### 2️⃣ Método `.format()`
```python
nome = 'Adriano'
preco = 1000.95897643
variavel = '{}, o preço é R${:.2f}'.format(nome, preco)
print(variavel)
print('O hexadecimal de {} é {:08X}'.format(1500, 1500))
```
🔹 **Saída:**
```
Adriano, o preço é R$1000.96
O hexadecimal de 1500 é 000005DC
```

### 3️⃣ F-strings (Python 3.6+)
```python
nome = 'Adriano'
preco = 1000.95897643
print(f'{nome}, o preço é R${preco:.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
```
🔹 **Saída:**
```
Adriano, o preço é R$1000.96
O hexadecimal de 1500 é 000005DC
```

## Flags de Conversão
```python
texto = 'Python'
print(f'Repr: {texto!r}')
print(f'Str: {texto!s}')
print(f'ASCII: {texto!a}')
```
🔹 **Saída:**
```
Repr: 'Python'
Str: Python
ASCII: 'Python'
```

## Alinhamento e Preenchimento
```python
print(f'|{"Texto":>10}|')  # Direita
print(f'|{"Texto":<10}|')  # Esquerda
print(f'|{"Texto":^10}|')  # Centralizado
print(f'|{1234:0>10}|')  # Preenchido com zeros à esquerda
```
🔹 **Saída:**
```
|     Texto|
|Texto     |
|  Texto   |
|0000001234|
```

## Exemplos Adicionais

### Interpolação com múltiplos valores
```python
nome = 'Carlos'
idade = 30
saldo = 259.75
print(f'Nome: {nome}, Idade: {idade}, Saldo: R${saldo:.2f}')
```
🔹 **Saída:**
```
Nome: Carlos, Idade: 30, Saldo: R$259.75
```

### Uso de variáveis dinâmicas dentro de F-strings
```python
for i in range(1, 6):
    print(f'Número {i:02}')
```
🔹 **Saída:**
```
Número 01
Número 02
Número 03
Número 04
Número 05
```

Essa abordagem detalhada facilita o entendimento e uso da interpolação de strings em Python. 🚀


"""