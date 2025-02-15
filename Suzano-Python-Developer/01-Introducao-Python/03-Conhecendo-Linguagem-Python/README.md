# Conhecendo a Linguagem Python

## Introdução
Python é uma linguagem de programação de alto nível, conhecida por sua sintaxe clara e fácil de aprender. Neste guia, exploraremos conceitos fundamentais para iniciar no desenvolvimento com Python.

---

## 1. Tipos de Dados
Python possui diversos tipos de dados embutidos que ajudam no desenvolvimento de aplicações. Alguns exemplos:
- **int** → Números inteiros (ex: `10`, `-3`, `1000`)
- **float** → Números de ponto flutuante (ex: `10.5`, `-2.7`)
- **str** → Cadeia de caracteres (ex: `'Olá, mundo!'`)
- **bool** → Valores booleanos (`True` ou `False`)
- **list** → Lista de elementos (ex: `[1, 2, 3, "texto"]`)
- **tuple** → Tupla imutável (ex: `(1, 2, 3)`)
- **dict** → Dicionário chave-valor (ex: `{"nome": "João", "idade": 30}`)
- **set** → Conjunto de elementos únicos (ex: `{1, 2, 3, 4}`)

Exemplo de uso:
```python
x = 10          # int
y = 3.14        # float
nome = "Alice"  # str
ativo = True    # bool
print(type(x), type(y), type(nome), type(ativo))
```

---

## 2. Modo Interativo
O Python permite a execução de comandos no modo interativo (REPL - Read Eval Print Loop). Para abrir o modo interativo, digite no terminal:
```sh
python
```
Você pode executar comandos diretamente, por exemplo:
```python
>>> 2 + 2
4
>>> print("Olá, Python!")
Olá, Python!
```
Para sair do modo interativo, digite:
```sh
exit()
```

---

## 3. Variáveis e Constantes
### **Variáveis**
As variáveis armazenam valores que podem ser modificados durante a execução do programa:
```python
idade = 25
nome = "Carlos"
print(nome, "tem", idade, "anos.")
```

### **Constantes**
Python não possui suporte nativo para constantes, mas por convenção, usamos nomes em MAIÚSCULAS para indicar que o valor não deve ser alterado:
```python
PI = 3.14159
GRAVIDADE = 9.81
```

---

## 4. Conversão de Tipos
Python permite a conversão entre diferentes tipos de dados:
```python
# Conversão de string para inteiro
num_str = "100"
num_int = int(num_str)

# Conversão de inteiro para string
num_texto = str(50)

# Conversão de float para inteiro
valor = int(10.5)
print(num_int, num_texto, valor)
```

Outras funções úteis para conversão:
- `float()` → Converte para ponto flutuante
- `bool()` → Converte para booleano
- `list()` → Converte para lista
- `tuple()` → Converte para tupla

---

## 5. Funções de Entrada e Saída
### **Entrada de Dados**
A função `input()` permite capturar informações do usuário:
```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

### **Saída de Dados**
A função `print()` exibe informações na tela:
```python
idade = 30
print(f"Você tem {idade} anos.")
```

**Formatando saída:**
```python
valor = 5.6789
print("O valor formatado é: {:.2f}".format(valor))
```

---

## Conclusão
Estes conceitos fundamentais são essenciais para iniciar com Python. Continue praticando para desenvolver suas habilidades na linguagem! 🚀

