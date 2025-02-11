# Conversão de Tipos em Python
# Em Python, podemos converter um tipo de dado para outro usando funções de type casting.

"""
Conversões Comuns
Função	    Descrição	                            Exemplo
int(x)	    Converte x para inteiro (int)	        int(3.9) → 3
float(x)	Converte x para número decimal (float)	float(10) → 10.0
str(x)	    Converte x para string (str)	        str(123) → "123"
bool(x)	    Converte x para booleano (bool)	        bool(1) → True, bool(0) → False
"""
# Convertendo números float e strings para inteiro
print(int(3.7))      # Saída: 3 (trunca a parte decimal)
print(int("42"))     # Saída: 42 (conversão de string para inteiro)
# print(int("Python")) # Erro! Não pode converter texto que não é número


# Convertendo inteiros e strings para float
print(float(10))        # Saída: 10.0
print(float("3.1415"))  # Saída: 3.1415


# Convertendo números e booleanos para string
print(str(100))      # Saída: '100'
print(str(3.14))     # Saída: '3.14'
print(str(True))     # Saída: 'True'

# Concatenando número com texto
idade = 25
print("Minha idade é " + str(idade))  # Correto: "Minha idade é 25"

# print("Minha idade é " + idade)  # Erro! str + int não são compatíveis


# Convertendo diferentes valores para booleano
print(bool(1))        # Saída: True
print(bool(0))        # Saída: False
print(bool(""))       # Saída: False (string vazia)
print(bool("Python")) # Saída: True (string não vazia)
print(bool(None))     # Saída: False


"""
Resumo
1. int(), float(), str(), bool() são usados para converter tipos de dados.
2. Strings contendo números podem ser convertidas ("42" → 42).
3. Valores vazios ("", 0, None) resultam em False quando convertidos para booleano.
4. Ao concatenar strings com números, sempre use str() para evitar erros.
"""