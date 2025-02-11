# Solicita ao usuário que escolha entre entrar ou sair
entrada = input('[E]ntrar [S]air: ').strip().upper()
senha_digitada = input('Digite a senha: ').strip()

# Definição da senha correta
SENHA_CORRETA = "123456"

# Verifica se a opção e a senha estão corretas
if entrada == 'E':
    if senha_digitada == SENHA_CORRETA:
        print('Acesso permitido. Bem-vindo!')
    else:
        print('Senha incorreta. Tente novamente.')
elif entrada == 'S':
    print('Saindo...')
else:
    print('Opção inválida. Digite "E" para entrar ou "S" para sair.')
