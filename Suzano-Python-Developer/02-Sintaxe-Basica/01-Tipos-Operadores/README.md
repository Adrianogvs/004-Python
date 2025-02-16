# Tipos de Dados em Python

## Introdução

Python é uma linguagem de programação dinamicamente tipada, o que significa que não é necessário declarar explicitamente o tipo de uma variável. Os tipos de dados são atribuídos automaticamente pelo interpretador com base no valor atribuído. A seguir, veremos os principais tipos de dados em Python com exemplos práticos.

---

## Tabela Resumo dos Tipos de Dados em Python

| Tipo de Dado | Descrição                  | Exemplo                          |
| ------------ | -------------------------- | -------------------------------- |
| `int`        | Números inteiros           | `10, -3, 1000`                   |
| `float`      | Números de ponto flutuante | `3.14, -2.5`                     |
| `complex`    | Números complexos          | `2+3j, -1j`                      |
| `bool`       | Valores booleanos          | `True, False`                    |
| `str`        | Sequências de caracteres   | `'Python', "Curso"`              |
| `list`       | Lista mutável de elementos | `[1, 2, "texto"]`                |
| `tuple`      | Tupla imutável             | `(1, 2, "Python")`               |
| `dict`       | Estrutura de chave-valor   | `{"nome": "Alice", "idade": 25}` |
| `set`        | Conjunto de valores únicos | `{1, 2, 3, 4}`                   |

---

## 1. **Tipos Numéricos**

Os tipos numéricos em Python incluem **inteiros (********`int`********)**, **ponto flutuante (********`float`********)** e **números complexos (********`complex`********)**.

### **Inteiros (********`int`********)**

```python
numero_inteiro = 10
print(type(numero_inteiro))  # <class 'int'>
```

### **Ponto Flutuante (********`float`********)**

```python
numero_float = 10.5
print(type(numero_float))  # <class 'float'>
```

### **Números Complexos (********`complex`********)**

```python
numero_complexo = 2 + 3j
print(type(numero_complexo))  # <class 'complex'>
```

---

## 2. **Precedência de Operadores**

A precedência dos operadores define a ordem de avaliação das expressões. A tabela abaixo mostra a ordem de precedência dos operadores em Python (do mais alto para o mais baixo):

| Precedência     | Operadores                                                             |   |
| --------------- | ---------------------------------------------------------------------- | - |
| 1 (Mais alto)   | `**` (Exponenciação)                                                   |   |
| 2               | `+x`, `-x`, `~x` (Unários)                                             |   |
| 3               | `*`, `/`, `//`, `%` (Multiplicação, divisão, divisão inteira e módulo) |   |
| 4               | `+`, `-` (Adição e subtração)                                          |   |
| 5               | `<<`, `>>` (Shift bits)                                                |   |
| 6               | `&` (AND bitwise)                                                      |   |
| 7               | `^` (XOR bitwise)                                                      |   |
| 8               | \`\` (OR bitwise)                                                      |   |
| 9               | `==`, `!=`, `>`, `<`, `>=`, `<=` (Comparação)                          |   |
| 10              | `is`, `is not`, `in`, `not in` (Identidade e associação)               |   |
| 11              | `not` (Negação lógica)                                                 |   |
| 12              | `and` (E lógico)                                                       |   |
| 13 (Mais baixo) | `or` (OU lógico)                                                       |   |

---

## 3. **Operadores de Comparação**

| Operador | Descrição        | Exemplo (`a = 10`, `b = 5`) |
| -------- | ---------------- | --------------------------- |
| `==`     | Igual a          | `a == b` → `False`          |
| `!=`     | Diferente de     | `a != b` → `True`           |
| `>`      | Maior que        | `a > b` → `True`            |
| `<`      | Menor que        | `a < b` → `False`           |
| `>=`     | Maior ou igual a | `a >= b` → `True`           |
| `<=`     | Menor ou igual a | `a <= b` → `False`          |

---

## 4. **Outros Tipos de Dados**

### **Strings (********`str`********)**

```python
texto = "Python é incrível!"
print(type(texto))  # <class 'str'>
```

### **Listas (********`list`********)**

```python
lista = [1, 2, 3, "Python"]
print(lista[0])  # 1
```

### **Dicionários (********`dict`********)**

```python
dicionario = {"nome": "Alice", "idade": 25}
print(dicionario["nome"])  # Alice
```

---

## 5. **Conversão de Tipos**

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

