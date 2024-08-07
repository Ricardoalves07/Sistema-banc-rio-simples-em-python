menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Erro: o valor do depósito deve ser positivo.")

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))

        saldo_insuficiente = valor_saque > saldo
        excede_limite = valor_saque > limite_diario
        excede_saques_diarios = numero_saques >= LIMITE_SAQUES_DIARIOS

        if saldo_insuficiente:
            print("Erro: saldo insuficiente.")
        elif excede_limite:
            print("Erro: o valor do saque excede o limite diário.")
        elif excede_saques_diarios:
            print("Erro: número máximo de saques diários excedido.")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        else:
            print("Erro: o valor do saque deve ser positivo.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Encerrando o sistema bancário. Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
