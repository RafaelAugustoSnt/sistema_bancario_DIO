saldo = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_POR_SAQUE = 500
quantidade_de_saque = 1
movimentacoes = []


while True:
    print("Bem vindo ao nosso banco o que gostaria de fazer hoje?")
    escolha = input(' [S]acar\n [D]epositar\n [E]xtrato\n [F]echar sistema: ')

    if escolha[0] == 'd' or escolha[0] == 'D':

        valor_deposito = input('Qual valor deseja depositar? ')

        if valor_deposito[0] == '-':
            print('Não é possivel depositar numero negativos')
            continue

        saldo += int(valor_deposito)

        movimentacoes.append(
            f'Foi depositado o valor de R${valor_deposito:.2f}'
            f' e o saldo da conta ficou R${saldo:.2f}')

        print(f'O seu saldo agora é de R${saldo:.2f}')

    elif escolha[0] == 's' or escolha[0] == 'S':

        if saldo == 0:
            print('A conta ainda não tem saldo')
            continue

        saque = int(input("Quanto você deseja sacar? "))

        if saque > saldo:
            print('O saque é maior que o valor na conta!')
            continue
        elif quantidade_de_saque > LIMITE_SAQUE_DIARIO:
            print('O limite de saques diarios foi atingidos!')
            continue
        elif saque > LIMITE_POR_SAQUE:
            print('O limite de valor do saque é de R$500,00')
            continue

        print('Sacando dinhero....')

        saldo -= saque
        quantidade_de_saque += 1
        movimentacoes.append(
            f'Foi sacado o valor de R${saque:.2f} e o saldo da conta ficou '
            f'em R${saldo:.2f}')

        print(
            f'Dinheiro sacado com sucesso, seu saldo agora é de R${saldo:.2f}'
        )

    elif escolha[0] == 'e' or escolha[0] == 'E':

        for movimentacao in movimentacoes:
            print(movimentacao)

        print(f"O Saldo da conta atual da conta é de R${saldo:.2f}")

    elif escolha == 'f' or escolha == 'F':
        break
    else:
        print('Opção inexistente! Escolha uma opção do menu')
        continue
