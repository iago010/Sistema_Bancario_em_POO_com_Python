import textwrap

from usuarios import filtrar_usuario, _normalizar_cpf


class Conta:
    def __init__(
        self,
        agencia,
        numero_conta,
        usuario,
        limite=500,
        limite_saques=3,
    ):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.limite = limite
        self.limite_saques = limite_saques
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print(
            "Não foram realizadas movimentações."
            if not self.extrato
            else self.extrato
        )
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

    def __str__(self):
        return (
            f"Agência: {self.agencia} | "
            f"Conta: {self.numero_conta} | "
            f"Titular: {self.usuario.nome}"
        )


def criar_conta(agencia, numero_conta, usuarios):
    cpf = _normalizar_cpf(input("Informe o CPF do usuário (somente número): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print(
            "\n@@@ Usuário não encontrado! "
            "Crie o usuário primeiro com [nu]. @@@"
        )
        return None  # retorno explícito para evitar None silencioso

    conta = Conta(agencia, numero_conta, usuario)
    print("\n=== Conta criada com sucesso! ===")
    return conta


def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return

    for conta in contas:
        linha = f"""\
Agência:\t{conta.agencia}
C/C:\t\t{conta.numero_conta}
Titular:\t{conta.usuario.nome}
"""
        print("=" * 100)
        print(textwrap.dedent(linha))
