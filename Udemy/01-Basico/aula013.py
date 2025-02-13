# Solicita ao usuário a entrada de dois valores numéricos
try:
    primeiro_valor = float(input('Digite o primeiro valor: '))
    segundo_valor = float(input('Digite o segundo valor: '))

    # Compara os valores e exibe o resultado
    if segundo_valor > primeiro_valor:
        print(f'O segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor}).')
    elif primeiro_valor > segundo_valor:
        print(f'O primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor}).')
    else:
        print('Os dois valores são iguais.')

except ValueError:
    print('Erro: Por favor, digite apenas números válidos.')
