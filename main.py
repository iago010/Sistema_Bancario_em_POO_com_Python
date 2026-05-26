from menu import menu
from usuarios import criar_usuario
from contas import criar_conta, listar_contas

AGENCIA = "0001"


def selecionar_conta(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return None

    try:
        numero_conta = int(input("Informe o número da conta: "))
    except ValueError:
        print("\n@@@ Número de conta inválido! @@@")
        return None

    for conta in contas:
        if conta.numero_conta == numero_conta:
            return conta

    print("\n@@@ Conta não encontrada! @@@")
    return None


def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "d":
            conta = selecionar_conta(contas)
            if conta:
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    conta.depositar(valor)
                except ValueError:
                    print("\n@@@ Valor inválido! @@@")

        elif opcao == "s":
            conta = selecionar_conta(contas)
            if conta:
                try:
                    valor = float(input("Informe o valor do saque: "))
                    conta.sacar(valor)
                except ValueError:
                    print("\n@@@ Valor inválido! @@@")

        elif opcao == "e":
            conta = selecionar_conta(contas)
            if conta:
                conta.exibir_extrato()

        elif opcao == "q":
            print("\nSaindo do sistema...")
            break

        else:
            print("\n@@@ Operação inválida! @@@")


main()
