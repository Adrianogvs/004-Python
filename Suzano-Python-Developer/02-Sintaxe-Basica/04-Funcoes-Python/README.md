# Funções

## Objetivo Geral
Entender como funcionam as funções em Python.

## Pré-requisitos
- Python 3
- VSCode

## Percurso
- Etapa 1: Estudo aprofundado sobre funções

## Etapa 1: Estudo aprofundado sobre funções
Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros. Esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código.

### O que são funções?
```python
# Definindo uma função simples
def saudacao():
    print("Olá, Mundo!")

saudacao()  # Chamada da função
```

### Retornando valores
```python
# Função que retorna um valor
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)  # 5
```
Em Python, uma função pode retornar mais de um valor:
```python
# Função retornando múltiplos valores
def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

s, d = operacoes(10, 5)
print(s, d)  # 15 5
```

### Argumentos nomeados
```python
# Utilizando argumentos nomeados
def exibir(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

exibir(nome="João", idade=30)
exibir(idade=25, nome="Maria")
```

### Args e Kwargs
```python
# Usando *args e **kwargs
def mostrar_informacoes(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)

mostrar_informacoes(1, 2, 3, nome="Ana", idade=22)
```

### Parâmetros especiais
- **Positional Only**: O argumento só pode ser passado por posição.
- **Keyword Only**: O argumento só pode ser passado como nomeado.
- **Keyword and Positional**: Pode ser passado tanto por posição quanto por nome.
```python
# Exemplo de parâmetros especiais
def exemplo(pos1, /, pos_nome, *, nome):
    print(pos1, pos_nome, nome)

exemplo(1, pos_nome=2, nome=3)  # Correto
```

### Objetos de primeira classe
Funções em Python são objetos de primeira classe, o que significa que podem ser atribuídas a variáveis, passadas como argumentos para outras funções e usadas como valores em estruturas de dados.
```python
# Funções como objetos de primeira classe
def cumprimentar(nome):
    return f"Olá, {nome}!"

saudacao = cumprimentar  # Atribuindo função a uma variável
print(saudacao("Pedro"))
```

### Escopo local e global
Em Python, as variáveis definidas dentro de uma função têm escopo local. Para utilizar variáveis globais, usa-se a palavra-chave `global`. No entanto, não é considerado uma boa prática.
```python
# Uso de variáveis globais (não recomendado)
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
```

