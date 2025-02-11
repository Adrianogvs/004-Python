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
idade = 40
altura = 1.85  # Corrigido para número decimal
peso = 110

def classificacao(peso, altura):
    # Função interna para calcular o IMC
    def calcular_imc(peso, altura):
        return peso / (altura ** 2)

    # Chamada da função de cálculo do IMC
    imc = calcular_imc(peso, altura)
    print(f"IMC calculado: {imc:.2f}")

    # Função interna para classificar o IMC
    def classificar_imc(imc):
        match imc:
            case _ if imc > 40:
                return 'Obesidade Grau III (mórbida)'
            case _ if 35 <= imc <= 40:
                return 'Obesidade Grau II (severa)'
            case _ if 30 <= imc < 35:
                return 'Obesidade Grau I'
            case _ if 25 <= imc < 30:
                return 'Sobrepeso'
            case _ if 18.5 <= imc < 25:
                return 'Peso normal'
            case _:
                return 'Abaixo do peso'

    # Retorna a classificação do IMC
    return classificar_imc(imc)

# Chamando a função principal e exibindo o resultado
resultado = classificacao(peso, altura)
print(f"A classificação do IMC de {nome} é: {resultado}")
