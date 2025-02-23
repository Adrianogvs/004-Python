# Indentação e Blocos

## Objetivo Geral
Aprender como o interpretador Python utiliza a indentação do código para delimitar os blocos de comandos.

## Pré-requisitos
- Python 3
- VSCode

## Percurso
- Etapa 1: Indentação e os blocos de comandos

## Etapa 1: Indentação e os blocos de comandos
### O papel da indentação
Identar código é uma forma de manter o código fonte mais legível e manutenível. Em Python, ela exerce um segundo papel: o interpretador utiliza a indentação para determinar onde um bloco de comando inicia e onde ele termina.

### A estética
Linguagens como Java e C utilizam caracteres (como chaves) para marcar o início e o fim de blocos de comandos. Já em Python, utiliza-se a indentação.

### Convenção em Python
Em Python, é indicado utilizar 4 espaços em branco por nível de indentação. Cada novo bloco adiciona 4 novos espaços.

### Exemplos de Blocos
```python
# Exemplo correto em Python
if True:
    print("Bloco identado corretamente")

# Exemplo incorreto em Python
if True:
print("Erro de identação")  # Isso gera um erro de identação em Python
```

---

# Estruturas Condicionais

## Objetivo Geral
Entender o que são as estruturas condicionais em Python e como utilizá-las.

## Pré-requisitos
- Python 3
- VSCode

## Percurso
- Etapa 1: If / if-else / elif
- Etapa 2: If aninhado
- Etapa 3: If ternário

## Etapa 1: If / if-else / elif
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

### If
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
```

### If/else
```python
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### If/elif/else
```python
nota = 85
if nota >= 90:
    print("Aprovado com excelência!")
elif nota >= 70:
    print("Aprovado.")
else:
    print("Reprovado.")
```

## Etapa 2: If aninhado
```python
idade = 20
habilitacao = True
if idade >= 18:
    if habilitacao:
        print("Pode dirigir.")
    else:
        print("Não pode dirigir.")
else:
    print("Menor de idade.")
```

## Etapa 3: If ternário
```python
idade = 18
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)
```

---

# Estruturas de Repetição

## Objetivo Geral
Conhecer as estruturas de repetição for e while e quando utilizá-las.

## Pré-requisitos
- Python 3
- VSCode

## Percurso
- Etapa 1: O que são estruturas de repetição?
- Etapa 2: Comando for e a função built-in range
- Etapa 3: Comando while

## Etapa 1: O que são estruturas de repetição?
Estruturas utilizadas para repetir um trecho de código um determinado número de vezes, conhecido previamente ou determinado através de uma expressão lógica.

## Etapa 2: Comando for e a função built-in range
```python
# Usando for com range
for i in range(5):
    print(i)  # Imprime de 0 a 4

# Usando for com lista
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)
```

## Etapa 3: Comando while
```python
# Usando while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

## Links Úteis
- [Trilha Python DIO](https://github.com/guicarvalho/trilha-python-dio)
- Fórum/Artigos
- Comunidade Online (Discord)

