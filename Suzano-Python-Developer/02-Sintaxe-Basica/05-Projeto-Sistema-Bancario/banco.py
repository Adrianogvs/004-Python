menu = """

Selecione uma das opções abaixo:
[s] = Saque
[d] = Deposito
[e] = Extrato
[q] = Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_sques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == 'd':
        print(f'Depósito')
    
    elif opcao == 's':
        print(f'Saque')
    
    elif opcao == 'e':
        print(f'Extrato')
    
    elif opcao == 'q':
        break

    else:
        print(f'Operação invalida, por favor selecione a operação desejada!')
    

