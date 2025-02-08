# Calclulo de IMC
"""
| Faixa de IMC        | Classificação      |
|---------------------|--------------------|
| Acima de 40,0       | Obesidade grau III |
| Entre 35,0 e 39,9   | Obesidade grau II  |
| Entre 30,0 e 34,9   | Obesidade grau I   |
| Entre 25,0 e 29,9   | Sobrepeso          |
| Entre 18,6 e 24,9   | Normal             |
| 18,5 ou menos       | Abaixo do normal   |
"""

nome = 'Adriano Vilela'
altura = 1.85
peso = 106
imc = 0 # imc = peso / (altura * altura)

nome = 'Adriano Vilela'
altura = 1.85
peso = 106

# Função para calcular o IMC
def calculo_imc(peso, altura):
    return peso / altura**2 

# Calcula o IMC antes de usar no match-case
imc = calculo_imc(peso, altura)

# Função para classificar o IMC
def classifica_imc(imc):
    match imc:
        case _ if 35 <= imc <= 40:
            return "IMC entre 35 e 40! (Obesidade Grau II)"
        case _ if 30 <= imc < 35:
            return "IMC entre 30 e 35! (Obesidade Grau I)"
        case _ if 25 <= imc < 30:
            return "IMC entre 25 e 30! (Sobrepeso)"
        case _ if 18.6 <= imc < 25:
            return "IMC normal!"
        case _:
            return "IMC abaixo do normal!"

# Exibe os resultados corretamente
print(f"Nome: {nome}")
print(f"IMC: {imc:.2f}")  
print(classifica_imc(imc))  

