# Solicita o salário e faz a conversão para float, tratando ',' como '.'
salario = float(input("Informe seu salário atual: R$ ").replace(",", ".").strip())

# Calcula o novo salário com 15% de aumento
novo_salario = salario * 1.15  

# Exibe o resultado formatado
print(f"Seu novo salário, com 15% de aumento, será de R$ {novo_salario:.2f}.")
