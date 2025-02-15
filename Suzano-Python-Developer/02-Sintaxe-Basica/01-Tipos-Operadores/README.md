# Tipos de Dados em Python

## Introdução
Python é uma linguagem de programação dinamicamente tipada, o que significa que não é necessário declarar explicitamente o tipo de uma variável. Os tipos de dados são atribuídos automaticamente pelo interpretador com base no valor atribuído. A seguir, veremos os principais tipos de dados em Python com exemplos práticos.

---

## 1. **Tipos Numéricos**
Os tipos numéricos em Python incluem **inteiros (`int`)**, **ponto flutuante (`float`)** e **números complexos (`complex`)**.

### **Inteiros (`int`)**
Números inteiros podem ser positivos ou negativos, sem parte decimal.
```python
numero_inteiro = 10
print(type(numero_inteiro))  # <class 'int'>
```

### **Ponto Flutuante (`float`)**
Números com casas decimais são representados pelo tipo `float`.
```python
numero_float = 10.5
print(type(numero_float))  # <class 'float'>
```

### **Números Complexos (`complex`)**
Números complexos têm uma parte real e uma parte imaginária, representada pelo sufixo `j`.
```python
numero_complexo = 2 + 3j
print(type(numero_complexo))  # <class 'complex'>
```

---

## 2. **Precedência de Operadores**
A precedência dos operadores define a ordem de avaliação das expressões. A tabela abaixo mostra a ordem de precedência dos operadores em Python (do mais alto para o mais baixo):

| Precedência | Operadores |
|-------------|-----------|
| 1 (Mais alto) | `**` (Exponenciação) |
| 2 | `+x`, `-x`, `~x` (Unários) |
| 3 | `*`, `/`, `//`, `%` (Multiplicação, divisão, divisão inteira e módulo) |
| 4 | `+`, `-` (Adição e subtração) |
| 5 | `<<`, `>>` (Shift bits) |
| 6 | `&` (AND bitwise) |
| 7 | `^` (XOR bitwise) |
| 8 | `|` (OR bitwise) |
| 9 | `==`, `!=`, `>`, `<`, `>=`, `<=` (Comparação) |
| 10 | `is`, `is not`, `in`, `not in` (Identidade e associação) |
| 11 | `not` (Negação lógica) |
| 12 | `and` (E lógico) |
| 13 (Mais baixo) | `or` (OU lógico) |

### **Exemplo de Precedência**
```python
resultado = 3 + 2 * 2
print(resultado)  # Saída: 7, pois a multiplicação ocorre primeiro
```

Se quiser mudar a precedência, use parênteses:
```python
resultado = (3 + 2) * 2
print(resultado)  # Saída: 10
```

---

## 3. **Tipo Booleano (`bool`)**
O tipo booleano representa os valores `True` ou `False`, usados principalmente em expressões condicionais.
```python
verdadeiro = True
falso = False
print(type(verdadeiro))  # <class 'bool'>
print(10 > 5)  # True
```

---

## 4. **Tipo String (`str`)**
Strings são sequências de caracteres, delimitadas por aspas simples (`'`) ou duplas (`"`).
```python
texto = "Python é incrível!"
print(type(texto))  # <class 'str'>
```

### **Principais Métodos para Strings**
```python
texto = " Aprendendo Python "
print(texto.lower())  # ' aprendendo python '
print(texto.upper())  # ' APRENDENDO PYTHON '
print(texto.strip())  # 'Aprendendo Python' (remove espaços extras)
print(texto.replace("Python", "Programação"))  # ' Aprendendo Programação '
```

---

## 5. **Estruturas de Dados em Python**

### **Listas (`list`)**
Listas são coleções ordenadas e mutáveis.
```python
lista = [1, 2, 3, "Python", True]
print(lista[2])  # 3
lista.append(4)  # Adiciona um elemento
print(lista)
```

### **Tuplas (`tuple`)**
Tuplas são coleções ordenadas e imutáveis.
```python
tupla = (1, 2, 3, "Python")
print(tupla[1])  # 2
```

### **Dicionários (`dict`)**
Dicionários armazenam pares de chave-valor.
```python
dicionario = {"nome": "Alice", "idade": 25}
print(dicionario["nome"])  # Alice
```

### **Conjuntos (`set`)**
Conjuntos armazenam valores únicos e não ordenados.
```python
conjunto = {1, 2, 3, 3, 4}
print(conjunto)  # {1, 2, 3, 4}
```

---

## 6. **Conversão de Tipos**
Python permite converter tipos de dados explicitamente.
```python
# De string para inteiro
numero = int("10")
print(numero, type(numero))  # 10 <class 'int'>

# De inteiro para string
texto = str(100)
print(texto, type(texto))  # '100' <class 'str'>
```

---

## Conclusão
Os tipos de dados em Python são fundamentais para manipulação de informações e desenvolvimento de aplicações. Praticar a conversão entre tipos, utilizar as estruturas de dados corretamente e entender a precedência dos operadores ajuda a tornar o código mais eficiente e organizado. 🚀

