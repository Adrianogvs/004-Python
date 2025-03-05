menu = """
Selecione uma das opções abaixo:
[s] = Saque
[d] = Depósito
[e] = Extrato
[q] = Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print(f"Operação falhou! O valor máximo por saque é R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 'e':
        print("\n===== EXTRATO =====")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===================\n")

    elif opcao == 'q':
        print("Saindo... Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")
