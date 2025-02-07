"""
📌 Operadores Aritméticos e Sua Precedência em Python
Em Python, os operadores aritméticos são usados para realizar cálculos matemáticos. Além disso, cada operador tem uma precedência, ou seja, uma ordem de execução.

📝 Operadores Aritméticos
Operador	Descrição	Exemplo	Resultado
+	Adição	10 + 5	15
-	Subtração	10 - 5	5
*	Multiplicação	10 * 5	50
/	Divisão (float)	10 / 4	2.5
//	Divisão inteira	10 // 4	2
%	Módulo (resto da divisão)	10 % 4	2
**	Exponenciação (potência)	2 ** 3	8
🔹 Exemplos:
"""

a = 10
b = 4

print(a + b)  # 14
print(a - b)  # 6
print(a * b)  # 40
print(a / b)  # 2.5
print(a // b) # 2  (divisão inteira)
print(a % b)  # 2  (resto da divisão)
print(2 ** 3) # 8  (2 elevado à 3)


"""
📌 Precedência dos Operadores
A precedência dos operadores define a ordem em que as operações são executadas. O Python segue esta ordem:

Ordem	Operador	Descrição
1️⃣	()	Parênteses (mais alta prioridade)
2️⃣	**	Exponenciação
3️⃣	*, /, //, %	Multiplicação, divisão, divisão inteira e módulo
4️⃣	+, -	Adição e subtração
🔹 Exemplo de Precedência:
"""

resultado = 10 + 3 * 2  # Multiplicação ocorre primeiro
print(resultado)  # Saída: 16

resultado = (10 + 3) * 2  # Parênteses têm maior prioridade
print(resultado)  # Saída: 26

resultado = 2 ** 3 * 4  # Exponenciação ocorre antes da multiplicação
print(resultado)  # Saída: 32


"""
🚀 Dica: Sempre Use Parênteses!
Mesmo que Python siga regras de precedência, é boa prática usar parênteses para tornar o código mais legível.
"""

# Melhor leitura com parênteses
resultado = (10 + 3) * 2  
print(resultado)  # Saída: 26