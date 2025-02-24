# Funções em Python

# O que são funções?
# Definindo uma função simples
def saudacao():
    print("Olá, Mundo!")

saudacao()  # Chamada da função

# Retornando valores
# Função que retorna um valor
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)  # 5

# Função retornando múltiplos valores
def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

s, d = operacoes(10, 5)
print(s, d)  # 15 5

# Argumentos nomeados
# Utilizando argumentos nomeados
def exibir(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

exibir(nome="João", idade=30)
exibir(idade=25, nome="Maria")

# Args e Kwargs
# Usando *args e **kwargs
def mostrar_informacoes(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)

mostrar_informacoes(1, 2, 3, nome="Ana", idade=22)

# Parâmetros especiais
# Exemplo de parâmetros especiais
def exemplo(pos1, /, pos_nome, *, nome):
    print(pos1, pos_nome, nome)

exemplo(1, pos_nome=2, nome=3)  # Correto

# Objetos de primeira classe
# Funções como objetos de primeira classe
def cumprimentar(nome):
    return f"Olá, {nome}!"

saudacao = cumprimentar  # Atribuindo função a uma variável
print(saudacao("Pedro"))

# Escopo local e global
# Uso de variáveis globais (não recomendado)
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
