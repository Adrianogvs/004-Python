"""
Introdução ao input() em Python
O input() é uma função embutida em Python que permite ao usuário inserir dados durante a execução do programa.
Ele retorna os dados inseridos pelo usuário como uma string.
"""

def exemplo_input_basico():
    variavel = input("Digite algo: ")
    print("Você digitou:", variavel)

# O argumento dentro de input() é opcional, mas geralmente é usado para exibir uma mensagem orientando o usuário.

def capturar_inteiro():
    """
    Capturando um número inteiro:
    Por padrão, input() retorna uma string, então é necessário converter para o tipo desejado.
    """
    try:
        idade = int(input("Digite sua idade: "))
        print(f"Sua idade é {idade} anos.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

def capturar_decimal():
    """
    Capturando um número decimal (float):
    Se quiser trabalhar com números decimais, use float().
    """
    try:
        altura = float(input("Digite sua altura (em metros): "))
        print(f"Sua altura é {altura:.2f} m")  # :.2f formata o número para exibir duas casas decimais.
    except ValueError:
        print("Erro: Digite um número decimal válido.")

def capturar_multiplos_valores():
    """
    Capturando múltiplos valores com split():
    O input() sempre retorna uma string, mas podemos dividir a entrada usando split().
    """
    try:
        nome, idade = input("Digite seu nome e idade separados por espaço: ").split()
        idade = int(idade)  # Converte idade para inteiro
        print(f"Nome: {nome}, Idade: {idade}")
    except ValueError:
        print("Erro: Certifique-se de inserir dois valores separados por espaço.")

def capturar_senha():
    """
    Solicitando uma senha sem exibi-la na tela:
    Para capturar senhas de forma segura, usamos a biblioteca getpass.
    """
    from getpass import getpass
    senha = getpass("Digite sua senha: ")
    print("Senha armazenada com sucesso!")

def verificar_numero():
    """
    Verificando se o usuário digitou um número:
    isdigit() retorna True apenas se a string contiver somente números.
    """
    entrada = input("Digite um número: ")
    if entrada.isdigit():
        numero = int(entrada)
        print(f"Você digitou o número {numero}.")
    else:
        print("Erro: Você não digitou um número válido.")

def loop_validacao():
    """
    Loop para garantir entrada válida:
    Se o usuário digitar algo inválido, o programa continuará pedindo até que um número válido seja inserido.
    """
    while True:
        entrada = input("Digite um número: ")
        if entrada.isdigit():
            numero = int(entrada)
            print(f"Você digitou o número {numero}.")
            break  # Sai do loop
        else:
            print("Erro: Digite um número válido.")

# Executando os exemplos um por um para fins didáticos
if __name__ == "__main__":
    exemplo_input_basico()
    capturar_inteiro()
    capturar_decimal()
    capturar_multiplos_valores()
    capturar_senha()
    verificar_numero()
    loop_validacao()
