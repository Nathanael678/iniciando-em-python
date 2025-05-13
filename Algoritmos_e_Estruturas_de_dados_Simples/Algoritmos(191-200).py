print("ALGORITMOS E ESTRUTURAS DE DADOS SIMPLES")

op = int(input("Escolha uma opção:"))

while op != 0:
    print(15 * "-+")
    print("0 = Sair")

    if op == 191:
        print("Você escolheu a opção 191")

        fila = []
        while True:
            print("1 - Inserir elemento")
            print("2 - Remover elemento")
            print("3 - Mostrar fila")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                elemento = input("Digite o elemento a ser inserido: ")
                fila.append(elemento)
                print(f"Elemento {elemento} inserido na fila.")
            elif opcao == 2:
                if fila:
                    elemento_removido = fila.pop(0)
                    print(f"Elemento {elemento_removido} removido da fila.")
                else:
                    print("A fila está vazia.")
            elif opcao == 3:
                print("Fila:", fila)
            elif opcao == 0:
                break
            else:
                print("Opção inválida!")

    elif op == 192:
        print("Você escolheu a opção 192")

        pilha = []
        while True:
            print("1 - Inserir elemento")
            print("2 - Remover elemento")
            print("3 - Mostrar pilha")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                elemento = input("Digite o elemento a ser inserido: ")
                pilha.append(elemento)
                print(f"Elemento {elemento} inserido na pilha.")
            elif opcao == 2:
                if pilha:
                    elemento_removido = pilha.pop()
                    print(f"Elemento {elemento_removido} removido da pilha.")
                else:
                    print("A pilha está vazia.")
            elif opcao == 3:
                print("Pilha:", pilha)
            elif opcao == 0:
                break
            else:
                print("Opção inválida!")

    elif op == 193:
        print("Você escolheu a opção 193")

        pilha = []
        while True:
            print("1 - Inserir número")
            print("2 - Adicionar")
            print("3 - Subtrair")
            print("4 - Multiplicar")
            print("5 - Dividir")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                numero = float(input("Digite o número a ser inserido: "))
                pilha.append(numero)
                print(f"Número {numero} inserido na pilha.")
            elif opcao == 2:
                if len(pilha) >= 2:
                    b = pilha.pop()
                    a = pilha.pop()
                    resultado = a + b
                    pilha.append(resultado)
                    print(f"Resultado da adição: {resultado}")
                else:
                    print("A pilha não tem números suficientes.")
            elif opcao == 3:
                if len(pilha) >= 2:
                    b = pilha.pop()
                    a = pilha.pop()
                    resultado = a - b
                    pilha.append(resultado)
                    print(f"Resultado da subtração: {resultado}")
                else:
                    print("A pilha não tem números suficientes.")
            elif opcao == 4:
                if len(pilha) >= 2:
                    b = pilha.pop()
                    a = pilha.pop()
                    resultado = a * b
                    pilha.append(resultado)
                    print(f"Resultado da multiplicação: {resultado}")
                else:
                    print("A pilha não tem números suficientes.")
            elif opcao == 5:
                if len(pilha) >= 2:
                    b = pilha.pop()
                    a = pilha.pop()
                    if b != 0:
                        resultado = a / b
                        pilha.append(resultado)
                        print(f"Resultado da divisão: {resultado}")
                    else:
                        print("Divisão por zero não é permitida.")
                        pilha.append(a)
                        pilha.append(b)
                else:
                    print("A pilha não tem números suficientes.")
            elif opcao == 0:
                break
            else:
                print("Opção inválida!")

    elif op == 194:
        print("Você escolheu a opção 194")

        fila = []
        while True:
            print("1 - Adicionar cliente")
            print("2 - Atender cliente")
            print("3 - Mostrar fila")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                cliente = input("Digite o nome do cliente: ")
                fila.append(cliente)
                print(f"Cliente {cliente} adicionado à fila.")
            elif opcao == 2:
                if fila:
                    cliente_atendido = fila.pop(0)
                    print(f"Cliente {cliente_atendido} atendido.")
                else:
                    print("A fila está vazia.")
            elif opcao == 3:
                print("Fila de atendimento:", fila)
            elif opcao == 0:
                break

    elif op == 195:
        print("Você escolheu a opção 195")

        import random
        cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        naipes = ["Copas", "Ouros", "Paus", "Espadas"]
        baralho = [f"{c} de {n}" for c in cartas for n in
        naipes]
        random.shuffle(baralho)
        while True:
            print("1 - Mostrar baralho")
            print("2 - Puxar carta")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                print("Baralho:", baralho)
            elif opcao == 2:
                if baralho:
                    carta_puxada = baralho.pop()
                    print(f"Carta puxada: {carta_puxada}")
                else:
                    print("O baralho está vazio.")
            elif opcao == 0:
                break
            else:
                print("Opção inválida!")
                
    elif op == 196:
        print("Você escolheu a opção 196")

        class Contato:
            def __init__(self, nome, telefone):
                self.nome = nome
                self.telefone = telefone
        agenda = []
        while True:
            print("1 - Adicionar contato")
            print("2 - Mostrar contatos")
            print("3 - Buscar contato")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                nome = input("Digite o nome do contato: ")
                telefone = input("Digite o telefone do contato: ")
                agenda.append(Contato(nome, telefone))
                print(f"Contato {nome} adicionado.")
            elif opcao == 2:
                for contato in agenda:
                    print(f"Nome: {contato.nome}, Telefone: {contato.telefone}")
            elif opcao == 3:
                nome_busca = input("Digite o nome do contato a buscar: ")
                for contato in agenda:
                    if contato.nome == nome_busca:
                        print(f"Contato encontrado: Nome: {contato.nome}, Telefone: {contato.telefone}")
                        break
                else:
                    print("Contato não encontrado.")
            elif opcao == 0:
                break

    elif op == 197:
        print("Você escolheu a opção 197")

        def busca_binaria(vetor, elemento):
            esquerda = 0
            direita = len(vetor) - 1
            while esquerda <= direita:
                meio = (esquerda + direita) // 2
                if vetor[meio] == elemento:
                    return meio
                elif vetor[meio] < elemento:
                    esquerda = meio + 1
                else:
                    direita = meio - 1
            return -1
        vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        elemento = int(input("Digite o elemento a buscar: "))
        resultado = busca_binaria(vetor, elemento)
        if resultado != -1:
            print(f"Elemento {elemento} encontrado na posição {resultado}.")
        else:
            print(f"Elemento {elemento} não encontrado no vetor.")
            
    elif op == 198:
        print("Você escolheu a opção 198")

        def ordenacao_insercao(vetor):
            for i in range(1, len(vetor)):
                chave = vetor[i]
                j = i - 1
                while j >= 0 and chave < vetor[j]:
                    vetor[j + 1] = vetor[j]
                    j -= 1
                vetor[j + 1] = chave
            return vetor
        vetor = [5, 2, 9, 1, 5, 6]
        print("Vetor original:", vetor)
        vetor_ordenado = ordenacao_insercao(vetor)
        print("Vetor ordenado:", vetor_ordenado)
        
    elif op == 199:
        print("Você escolheu a opção 199")

        import time
        def bubble_sort(vetor):
            n = len(vetor)
            for i in range(n):
                for j in range(0, n-i-1):
                    if vetor[j] > vetor[j+1]:
                        vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
            return vetor
        def selection_sort(vetor):
            n = len(vetor)
            for i in range(n):
                min_idx = i
                for j in range(i+1, n):
                    if vetor[j] < vetor[min_idx]:
                        min_idx = j
                vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
            return vetor
        vetor = [64, 34, 25, 12, 22, 11, 90]
        print("Vetor original:", vetor)
        start_time = time.time()
        vetor_bubble = bubble_sort(vetor.copy())
        end_time = time.time()
        print("Vetor ordenado com Bubble Sort:", vetor_bubble)
        print("Tempo de execução:", end_time - start_time)
        start_time = time.time()
        vetor_selection = selection_sort(vetor.copy())
        end_time = time.time()
        print("Vetor ordenado com Selection Sort:", vetor_selection)
        print("Tempo de execução:", end_time - start_time)
        
    elif op == 200:
        print("Você escolheu a opção 200")

        cardapio = {
            "1": "Hamburguer",
            "2": "Batata Frita",
            "3": "Refrigerante",
            "4": "Pizza",
            "5": "Salada"
        }
        pedidos = []
        fila_producao = []
        while True:
            print("Cardápio:")
            for key, value in cardapio.items():
                print(f"{key} - {value}")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao in cardapio:
                pedidos.append(cardapio[opcao])
                fila_producao.append(cardapio[opcao])
                print(f"Pedido {cardapio[opcao]} adicionado à fila de produção.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")
                

    else:
        print("Opção inválida!")
    print(15 * "-+")
    print("0 = Sair")
    op = int(input("Esolha uma opção de 141 a 170: "))
    if op == 0:
        print("Saindo...")
        break