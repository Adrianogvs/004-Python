# Sintaxe Básica do Python

## Introdução
Esta seção cobre os fundamentos essenciais da sintaxe da linguagem Python. Aprender esses conceitos é fundamental para o desenvolvimento de aplicações robustas e bem estruturadas.

---

## Estrutura da Pasta e Conteúdo Detalhado

### 1. **Tipos e Operadores**
Python oferece diversos tipos de dados e operadores para manipulação de valores.

#### **Tipos de Dados**
- `int` → Números inteiros (ex: `10`, `-3`)
- `float` → Números decimais (ex: `3.14`, `-2.5`)
- `str` → Texto (ex: `'Python'`, `"Curso"`)
- `bool` → Valores booleanos (`True`, `False`)

#### **Operadores Matemáticos**
```python
x = 10
y = 3
print(x + y)  # Adição
print(x - y)  # Subtração
print(x * y)  # Multiplicação
print(x / y)  # Divisão
print(x ** y) # Exponenciação
```

#### **Operadores de Comparação**
```python
print(10 > 5)  # True
print(10 == 5) # False
print(10 != 5) # True
```

#### **Operadores Lógicos**
```python
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---

### 2. **Estruturas Condicionais e Repetição**
Controle de fluxo em Python permite tomar decisões e repetir ações.

#### **Condicionais (`if`, `elif`, `else`)**
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade")
elif idade == 17:
    print("Falta um ano para a maioridade")
else:
    print("Você é menor de idade")
```

#### **Laços de Repetição**

##### **Laço `for`**
```python
for i in range(5):
    print(f"Número: {i}")
```

##### **Laço `while`**
```python
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
```

---

### 3. **Manipulando Strings**
Strings em Python possuem métodos úteis para manipulação de texto.

#### **Concatenação e Fatiamento**
```python
nome = "Python"
versao = "3.10"
print(nome + " versão " + versao)  # Concatenação
print(nome[0:3])  # Fatiamento ("Pyt")
```

#### **Métodos de Strings**
```python
texto = " Olá, Mundo! "
print(texto.strip())  # Remove espaços
print(texto.lower())  # Converte para minúsculas
print(texto.upper())  # Converte para maiúsculas
print(texto.replace("Mundo", "Python"))  # Substituição
```

---

### 4. **Funções em Python**
Funções permitem reutilizar código e modularizar programas.

#### **Definição e Chamada de Funções**
```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Carlos"))
```

#### **Funções com Valores Padrão**
```python
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(3))  # Usa o valor padrão (3^2)
print(potencia(3, 3))  # 3^3
```

---

### 5. **Projeto: Sistema Bancário**
Aplicação prática utilizando os conceitos aprendidos.

#### **Descrição**
Criamos um sistema bancário que permite:
- Depósito
- Saque
- Visualização de saldo

#### **Código Exemplo**
```python
class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}"
        else:
            return "Saldo insuficiente."

    def ver_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

# Exemplo de uso
conta = ContaBancaria(1000)
print(conta.depositar(500))
print(conta.sacar(200))
print(conta.ver_saldo())
```

---

## Como Utilizar
1. Clone o repositório ou acesse os arquivos diretamente.
2. Navegue pelos diretórios e abra os arquivos em um editor de código como VS Code ou PyCharm.
3. Execute os scripts para testar e modificar conforme necessário.

```sh
# Clonando o repositório
git clone https://github.com/seu-repositorio.git
cd 02-Sintaxe-Basica
```

4. Experimente modificar os códigos e executar os exemplos para melhor compreensão.

---

## Conclusão
Dominar a sintaxe básica do Python é o primeiro passo para se tornar um desenvolvedor eficiente. Continue praticando e aprofundando seus conhecimentos com projetos práticos! 🚀

