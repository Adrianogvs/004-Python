# Valores booleanos
verdadeiro = True
falso = False

print(type(verdadeiro))  # <class 'bool'>
print(type(falso))  # <class 'bool'>

# Comparações que retornam booleanos
print(10 > 5)  # True
print(3 == 5)  # False
print("Python" != "Java")  # True

# Booleanos em condições
idade = 18
maior_de_idade = idade >= 18

if maior_de_idade:
    print("Pode entrar!")  # Será exibido pois a condição é True
else:
    print("Acesso negado!")

# Convertendo valores para booleano
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False (string vazia é considerada False)
print(bool("Python"))  # True (string não vazia é True)
