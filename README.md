# 🏦 Sistema Bancário em Python

> Projeto desenvolvido com fins **didáticos** para estudo e prática de **Programação Orientada a Objetos (POO)** em Python.

---

## 📚 Sobre o Projeto

Este sistema simula operações básicas de um banco, como cadastro de usuários, abertura de contas, depósitos, saques e exibição de extratos. O foco do projeto é demonstrar na prática os conceitos fundamentais da POO, como **classes**, **objetos**, **encapsulamento** e **separação de responsabilidades** entre módulos.

---

## 🗂️ Estrutura do Projeto

```
banco/
├── main.py        # Ponto de entrada da aplicação e fluxo principal
├── menu.py        # Exibição e leitura do menu interativo
├── usuarios.py    # Classe Usuario e funções de cadastro/busca
├── contas.py      # Classe Conta e funções de criação/listagem
└── README.md
```

---

## ⚙️ Funcionalidades

| Opção | Descrição |
|-------|-----------|
| `[nu]` | Cadastrar novo usuário |
| `[nc]` | Abrir nova conta corrente |
| `[lc]` | Listar todas as contas |
| `[d]`  | Realizar depósito |
| `[s]`  | Realizar saque |
| `[e]`  | Exibir extrato |
| `[q]`  | Sair do sistema |

---

## 🧩 Conceitos de POO Aplicados

- **Classe e Objeto** — `Usuario` e `Conta` são classes que representam entidades do mundo real
- **Atributos de instância** — cada conta tem seu próprio saldo, extrato e número de saques
- **Métodos** — comportamentos encapsulados como `depositar()`, `sacar()` e `exibir_extrato()`
- **Encapsulamento** — cada módulo cuida apenas da sua própria responsabilidade
- **Separação de responsabilidades** — lógica de usuários, contas e interface separadas em arquivos distintos

---

## ▶️ Como Executar

Certifique-se de ter o **Python 3.8+** instalado. Todos os arquivos devem estar na mesma pasta.

```bash
python main.py
```

Siga o fluxo recomendado:

1. Cadastre um usuário com **`[nu]`**
2. Crie uma conta com **`[nc]`** informando o CPF cadastrado
3. Use as demais opções para operar a conta

---

## 📌 Regras de Negócio

- Não é possível criar uma conta sem um usuário previamente cadastrado
- Cada conta possui limite de saque de **R$ 500,00** por operação
- São permitidos no máximo **3 saques** por sessão
- O CPF é aceito com ou sem formatação (pontos e traços são ignorados automaticamente)

---

## 🛠️ Tecnologias

- Python 3.8+
- Biblioteca padrão (`textwrap`)
- Nenhuma dependência externa

---

## 📖 Fins Didáticos

Este projeto faz parte de um estudo prático de POO em Python. O código foi estruturado de forma propositalmente simples e legível para facilitar o aprendizado. Não é recomendado para uso em produção.
