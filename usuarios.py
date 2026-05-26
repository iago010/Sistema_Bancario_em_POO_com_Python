class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


def _normalizar_cpf(cpf):
    """Remove pontos, traços e espaços do CPF."""
    return "".join(filter(str.isdigit, cpf))


def filtrar_usuario(cpf, usuarios):
    cpf = _normalizar_cpf(cpf)
    usuarios_filtrados = [u for u in usuarios if u.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = _normalizar_cpf(input("Informe o CPF (somente número): "))

    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    novo_usuario = Usuario(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        endereco=endereco,
    )
    usuarios.append(novo_usuario)
    print("\n=== Usuário criado com sucesso! ===")
