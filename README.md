# 📌 Introdução ao Python

## 🔹 O que é Python?

Python é uma linguagem de programação de alto nível, de sintaxe simples e legível. É amplamente usada em diversas áreas como desenvolvimento web, análise de dados, inteligência artificial e automação.

---

# 📝 **Variáveis em Python**

Variáveis são espaços na memória que armazenam valores. Elas podem conter diferentes tipos de dados, como números, strings, listas, etc.

## 🔹 **Criando Variáveis**

```python
nome = "Maria"  # String (texto)
idade = 30  # Inteiro
altura = 1.65  # Float (número decimal)
ativo = True  # Booleano (True ou False)
```

## 🔹 **Regras para nomes de variáveis**

✅ Devem **começar com uma letra** ou **underscore (****`_`****)**\
✅ Podem conter letras, números e underscores (`_`)\
✅ **Não podem começar com números**\
✅ Python **diferencia maiúsculas e minúsculas** (`idade` ≠ `Idade`)\
✅ **Não podem ser palavras reservadas** (exemplo: `def`, `class`, `if`, etc.)

### ✅ **Exemplos válidos**:

```python
nome_completo = "Carlos Silva"
_idade = 28
altura_pessoa = 1.80
```

### ❌ **Exemplos inválidos**:

```python
2nome = "João"  # ❌ Começa com número
nome completo = "Ana"  # ❌ Espaços não são permitidos
```

---

# 📌 **Tipos de Dados em Python**

Python possui diversos tipos de dados. Alguns dos mais comuns:

## 🔹 **Tipos Numéricos (****`int`**** e ****`float`****)**

```python
numero_inteiro = 7  # int
numero_decimal = 3.14  # float
```

## 🔹 **Texto (****`str`****)**

```python
mensagem = "Python é incrível!"
print(mensagem[0])  # Saída: P
```

## 🔹 **Booleanos (****`bool`****)**

```python
ativo = True
print(bool(0))  # Saída: False
print(bool("Python"))  # Saída: True
```

---

# 🎨 **PEP 8 – Convenções de Estilo para Python**

## 🔹 **Nomeação de Variáveis**

✅ Use **nomes descritivos** e **minúsculas com underscores (****`_`****)**

```python
# Correto ✅
nome_completo = "Carlos Silva"

# Errado ❌
NomeCompleto = "Carlos Silva"  # Evite CamelCase
```

## 🔹 **Identação (4 espaços)**

```python
# Correto ✅
def somar(a, b):
    resultado = a + b
    return resultado
```

## 🔹 **Importações separadas**

```python
# Correto ✅
import os
import sys
```

---

# 📌 **Conversão de Tipos (Type Casting)**

## 🔹 **Principais Funções de Conversão**

| Função     | Descrição              | Exemplo            |
| ---------- | ---------------------- | ------------------ |
| `int(x)`   | Converte para inteiro  | `int(3.9) → 3`     |
| `float(x)` | Converte para float    | `float(10) → 10.0` |
| `str(x)`   | Converte para string   | `str(123) → "123"` |
| `bool(x)`  | Converte para booleano | `bool(1) → True`   |

## 🔹 **Exemplos**

```python
print(int(3.7))  # 3
print(float("3.14"))  # 3.14
print(str(100))  # '100'
print(bool(0))  # False
```

---

# 📌 **Operadores Aritméticos e Precedência**

## 🔹 **Operadores Aritméticos**

| Operador | Descrição       | Exemplo   | Resultado |
| -------- | --------------- | --------- | --------- |
| `+`      | Adição          | `10 + 5`  | `15`      |
| `-`      | Subtração       | `10 - 5`  | `5`       |
| `*`      | Multiplicação   | `10 * 5`  | `50`      |
| `/`      | Divisão         | `10 / 4`  | `2.5`     |
| `//`     | Divisão inteira | `10 // 4` | `2`       |
| `%`      | Módulo          | `10 % 4`  | `2`       |
| `**`     | Exponenciação   | `2 ** 3`  | `8`       |

## 🔹 **Precedência dos Operadores**

| Ordem | Operador            | Descrição                                            |
| ----- | ------------------- | ---------------------------------------------------- |
| 1️⃣   | `()`                | **Parênteses** (maior prioridade)                    |
| 2️⃣   | `**`                | **Exponenciação**                                    |
| 3️⃣   | `*`, `/`, `//`, `%` | **Multiplicação, divisão, divisão inteira e módulo** |
| 4️⃣   | `+`, `-`            | **Adição e subtração**                               |

## 🔹 **Exemplo de Precedência**

```python
resultado = 10 + 3 * 2  # Multiplicação ocorre primeiro
print(resultado)  # Saída: 16

resultado = (10 + 3) * 2  # Parênteses têm maior prioridade
print(resultado)  # Saída: 26
```

---

# 🚀 **Conclusão**

Este documento apresentou conceitos fundamentais do Python, como **variáveis, tipos de dados, conversão de tipos, PEP 8, operadores aritméticos e sua precedência**.

Python é uma linguagem poderosa e flexível. Quanto mais você pratica, mais fluente se torna! 🎯🚀

