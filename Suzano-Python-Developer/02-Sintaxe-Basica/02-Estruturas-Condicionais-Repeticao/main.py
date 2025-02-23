
# Indentação e Blocos

# Exemplo correto em Python
if True:
    print("Bloco identado corretamente")

# Exemplo incorreto em Python
# if True:
# print("Erro de identação")  # Isso gera um erro de identação em Python


# Estruturas Condicionais

# If
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

# If/else
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# If/elif/else
nota = 85
if nota >= 90:
    print("Aprovado com excelência!")
elif nota >= 70:
    print("Aprovado.")
else:
    print("Reprovado.")

# If aninhado
idade = 20
habilitacao = True
if idade >= 18:
    if habilitacao:
        print("Pode dirigir.")
    else:
        print("Não pode dirigir.")
else:
    print("Menor de idade.")

# If ternário
idade = 18
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)


# Estruturas de Repetição

# Usando for com range
for i in range(5):
    print(i)  # Imprime de 0 a 4

# Usando for com lista
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Usando while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
