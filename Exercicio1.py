class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contadorV = 1
        self.contadorA = 201

    def inserirSemPrioridade(self, nodo):
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").upper()
        if cor == 'V':
            numero = self.contadorV
            self.contadorV += 1
        elif cor == 'A':
            numero = self.contadorA
            self.contadorA += 1
        else:
            print("Cor inválida. Digite apenas A ou V.")
            return

        novo = Nodo(numero, cor)

        if self.head is None:
            self.head = novo
        elif cor == 'V':
            self.inserirSemPrioridade(novo)
        else:
            self.inserirComPrioridade(novo)

        print(f"Paciente com cartão {cor}{numero} adicionado à fila.")

    def imprimirListaEspera(self):
        atual = self.head
        print("\n--- Lista de Espera ---")
        if atual is None:
            print("Fila vazia.")
        else:
            while atual is not None:
                print(f"Cartão {atual.cor}{atual.numero}")
                atual = atual.proximo
        print("------------------------\n")

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila.")
        else:
            atendido = self.head
            self.head = self.head.proximo
            print(f"Chamando paciente do cartão {atendido.cor}{atendido.numero} para atendimento.")


def menu():
    fila = ListaEncadeada()
    while True:
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input("> ")

        if opcao == '1':
            fila.inserir()
        elif opcao == '2':
            fila.imprimirListaEspera()
        elif opcao == '3':
            fila.atenderPaciente()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, tente novamente.")


# Iniciar o menu
menu()
