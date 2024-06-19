menu = """
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Encerrar
"""

saldo = 0.0
VALOR_MAXIMO_POR_SAQUE = 500
qtd_saques = 0
NUM_LIMITE_SAQUES = 3
extrato = ""

while True:

    opcao = input(menu)

    if opcao.upper() == 'D':
        print("Depositar")
        deposito = float(input("Informe o valor a ser depositado R$ "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de R$ {deposito:.2f}\n"

        else:
            print("Erro ao realizar operação. Valor inválido")

    elif opcao.upper() == "S":
        print("Sacar")
        if(qtd_saques < NUM_LIMITE_SAQUES):
            valor_saque = float(input("Informe o valor do saque R$ "))
            if valor_saque <= 0:
                print("Erro ao realizar operação. Valor inválido")

            elif valor_saque > VALOR_MAXIMO_POR_SAQUE:
                print("Erro ao realizar operação. Valor solicitado ultrapassa valor limite por saque")

            elif valor_saque > saldo:
                print("Erro ao realizar operação. Valor solicitaod ultrapassa saldo disponível")

            else:
                qtd_saques += 1
                saldo -= valor_saque
                extrato += f"Saque de R$ {valor_saque:.2f}\n"

        else:
            print("Erro ao realizar operação. Número máximo de saques atingido.")


    elif opcao.upper() == "E":
        print("Extrato")
        print(extrato)
        print(f"\nO saldo atual é de R$ {saldo:.2f}\n")
    
    elif opcao.upper() == "Q":
        print("Encerrar")
        break
    
    else:
        print("Opção inválida!")
