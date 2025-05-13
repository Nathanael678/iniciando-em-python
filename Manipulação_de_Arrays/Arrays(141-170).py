print("ARRAYS E MATRIZES")

op = int(input("Esolha uma opção de 141 a 170: "))

while op != 0:
    print(15 * "-+")
    print("0 = Sair")

    if op == 141:
        print("Você escolheu a opção 141")


        vetor = []
        for i in range(10):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor:", vetor)

    elif op == 142:
        print("Você escolheu a opção 142")

        vetor = []
        for i in range(4):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
            media = sum(vetor) / len(vetor)
        print("Vetor:", vetor)
        print("Média:", media)

    elif op == 143:
        print("Você escolheu a opção 143")

        vetor = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor:", vetor)
        maior = max(vetor)
        menor = min(vetor)
        print("Maior valor:", maior)
        print("Menor valor:", menor)

    elif op == 144:
        print("Você escolheu a opção 144")

        array1 = []
        array2 = []
        for i in range(4):
            valor1 = int(input(f"Digite o valor para a posição {i} do primeiro vetor: "))
            array1.append(valor1)
            print(f"Valor {valor1} adicionado na posição {i} do primeiro vetor")
            valor2 = int(input(f"Digite o valor para a posição {i} do segundo vetor: "))
            array2.append(valor2)
            print(f"Valor {valor2} adicionado na posição {i} do segundo vetor")
        print("Primeiro vetor:", array1)
        print("Segundo vetor:", array2)
        soma = [a + b for a, b in zip(array1, array2)]
        print("Soma dos vetores:", soma)
    
    elif op == 145:
        print("Você escolheu a opção 145")

        vetor = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor:", vetor)
        vetor.sort(reverse=True)
        print("Vetor ordenado em ordem decrescente:", vetor)

    elif op == 146:
        print("Você escolheu a opção 146")

        vetor_negativo = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor_negativo.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor:", vetor_negativo)
        vetor_positivo = [valor for valor in vetor_negativo if valor > 0]
        print("Vetor positivo:", vetor_positivo)
        vetor_negativo = [valor for valor in vetor_negativo if valor < 0]
        print("Vetor negativo:", vetor_negativo)

    elif op == 147:
        print("Você escolheu a opção 147")

        def verificar_repetidos(vetor):
            for i in range(len(vetor)):
                for j in range(i + 1, len(vetor)):
                    if vetor[i] == vetor[j]:
                        return True
            return False

        vetor = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor:", vetor)
        if verificar_repetidos(vetor):
            print("O vetor contém valores repetidos.")
        else:
            print("O vetor não contém valores repetidos.")        

    elif op == 148:
        print("Você escolheu a opção 148")

        vetor_nomes = []
        for i in range(5):
            nome = input(f"Digite o nome para a posição {i}: ")
            vetor_nomes.append(nome)
            print(f"Nome {nome} adicionado na posição {i}")
        print("Vetor de nomes:", vetor_nomes)
        reversa = vetor_nomes[::-1]
        print("Vetor de nomes em ordem reversa:", reversa)

    elif op == 149:
        print("Você escolheu a opção 149")

        vetor = []
        while True:
            valor = int(input(f"Digite um valor (ou -1 para encerrar): "))
            if valor == -1:
                break
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {len(vetor)-1}")

        print("Vetor:", vetor)

        if vetor:  # Evita divisão por zero
            media = sum(vetor) / len(vetor)
            print("Média:", media)
        else:
            print("Nenhum valor foi inserido.")

    elif op == 150:
        print("Você escolheu a opção 150")

        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz:")
        for linha in matriz:
            print(linha)

    elif op == 151:
        print("Você escolheu a opção 151")


        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz:")
        for linha in matriz:
            print(linha)
        soma_diagonal = 0
        for i in range(3):
            soma_diagonal += matriz[i][i]
        print("Soma da diagonal principal:", soma_diagonal)

    elif op == 152:
        print("Você escolheu a opção 152")

        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz:")
        for linha in matriz:
            print(linha)
        soma_diagonal_secundaria = 0
        for i in range(3):
            soma_diagonal_secundaria += matriz[i][2 - i]
        print("Soma da diagonal secundária:", soma_diagonal_secundaria)

    elif op == 153:
        print("Você escolheu a opção 153")

        matriz = [] 
        for i in range(4):
            linha = []
            for j in range(4):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz:")
        for linha in matriz:
            print(linha)
        soma_linhas = []
        for i in range(4):
            soma_linha = 0
            for j in range(4):
                soma_linha += matriz[i][j]
            soma_linhas.append(soma_linha)
        print("Soma de cada linha:", soma_linhas)
    
    elif op == 154:
        print("Você escolheu a opção 154")

        matriz = []
        for i in range(4):
            linha = []
            for j in range(4):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz:")
        for linha in matriz:
            print(linha)
        soma_colunas = []
        for j in range(4):
            soma_coluna = 0
            for i in range(4):
                soma_coluna += matriz[i][j]
            soma_colunas.append(soma_coluna)
        print("Soma de cada coluna:", soma_colunas)
        
    elif op == 155:
        print("Você escolheu a opção 155")

        matriz = []
        for i in range(4):
            linha = []
            for j in range(4):
                if i == j:
                    linha.append(1)
                else:
                    linha.append(0)
                print(f"Valor {linha[j]} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz identidade:")
        for linha in matriz:
            print(linha)
            
    elif op == 156:
        print("Você escloheu a opção 156")

        def eh_simples(matriz):
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] != 0 and i != j:
                        return False
            return True

        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz:")
        for linha in matriz:
            print(linha)
        if eh_simples(matriz):
            print("A matriz é simples.")
        else:
            print("A matriz não é simples.")

    elif op == 157:
        print("Você escolheu a opção 157")

        matriz1 = []
        matriz2 = []
        for i in range(2):
            linha = []
            for j in range(2):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}] da primeira matriz: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}] da primeira matriz")
            matriz1.append(linha)
        for i in range(2):
            linha = []
            for j in range(2):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}] da segunda matriz: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}] da segunda matriz")
            matriz2.append(linha)
        print("Primeira matriz:")
        for linha in matriz1:
            print(linha)
        print("Segunda matriz:")
        for linha in matriz2:
            print(linha)
        matriz_resultado = []
        for i in range(2):
            linha = []
            for j in range(2):
                valor = 0
                for k in range(2):
                    valor += matriz1[i][k] * matriz2[k][j]
                linha.append(valor)
            matriz_resultado.append(linha)
        print("Matriz resultado:")
        for linha in matriz_resultado:
            print(linha)
            
    elif op == 158:
        print("Você escolheu a opção 158")

        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz original:")
        for linha in matriz:
            print(linha)
        for i in range(0, 3, 2):
            if i + 1 < 3:
                matriz[i], matriz[i + 1] = matriz[i + 1], matriz[i]
        print("Matriz com linhas trocadas:")
        for linha in matriz:
            print(linha)
            
    elif op == 159:
        print("Você escolheu a opção 159")

        matriz = []
        for i in range(1, 11):
            linha = []
            for j in range(1, 11):
                linha.append(i * j)
            matriz.append(linha)
        print("Tabela de multiplicação:")
        for linha in matriz:
            print(linha)
            
    elif op == 160:
        print("VoCê escolheu a opção 160")

        matriz = []
        for i in range(3):
            linha = []
            for j in range(4):
                valor = float(input(f"Digite a nota do aluno {i + 1} na prova {j + 1}: "))
                linha.append(valor)
                print(f"Nota {valor} adicionada na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz de notas:")
        for linha in matriz:
            print(linha)
        medias = []
        for i in range(3):
            soma = 0
            for j in range(4):
                soma += matriz[i][j]
            media = soma / 4
            medias.append(media)
        print("Médias dos alunos:", medias)

    elif op == 161:
        print("Você escolheu a opção 161")

        def eh_quadrado_magico(matriz):
            soma_diagonal1 = sum(matriz[i][i] for i in range(3))
            soma_diagonal2 = sum(matriz[i][2 - i] for i in range(3))
            if soma_diagonal1 != soma_diagonal2:
                return False
            for i in range(3):
                if sum(matriz[i]) != soma_diagonal1:
                    return False
                if sum(matriz[j][i] for j in range(3)) != soma_diagonal1:
                    return False
            return True
        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                linha.append(valor)
                print(f"Valor {valor} adicionado na posição [{i}][{j}]")
            matriz.append(linha)
        print("Matriz:")
        for linha in matriz:
            print(linha)
        if eh_quadrado_magico(matriz):
            print("A matriz é um quadrado mágico.")

    elif op == 162:
        print("Você escolheu a opção 162")

        vetor = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor original:", vetor)
        for i in range(len(vetor)):
            menor = i
            for j in range(i + 1, len(vetor)):
                if vetor[j] < vetor[menor]:
                    menor = j
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
        print("Vetor ordenado:", vetor)
        
    elif op == 163:
        print("Você escolheu a opção 163")

        import random
        n = int(input("Digite o tamanho do vetor: "))
        vetor = [random.randint(1, 10) for _ in range(n)]
        print("Vetor gerado:", vetor)
        print("Soma dos elementos do vetor:", sum(vetor))
        print("Média dos elementos do vetor:", sum(vetor) / n)
        
    elif op == 164:
        print("Você escolheu a opção 164")

        def sao_iguais(vetor1, vetor2):
            if len(vetor1) != len(vetor2):
                return False
            for i in range(len(vetor1)):
                if vetor1[i] != vetor2[i]:
                    return False
            return True
        vetor1 = []
        vetor2 = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i} do primeiro vetor: "))
            vetor1.append(valor)
            print(f"Valor {valor} adicionado na posição {i} do primeiro vetor")
            valor = int(input(f"Digite o valor para a posição {i} do segundo vetor: "))
            vetor2.append(valor)
            print(f"Valor {valor} adicionado na posição {i} do segundo vetor")
        print("Primeiro vetor:", vetor1)
        print("Segundo vetor:", vetor2)
        if sao_iguais(vetor1, vetor2):
            print("Os vetores são iguais.")
        else:
            print("Os vetores não são iguais.")
            
    elif op == 165:
        print("Você escolheu a opção 165")

        vetor = []
        for i in range(5):
            nome = input(f"Digite o nome da pessoa {i + 1}: ")
            nota1 = float(input(f"Digite a nota 1 de {nome}: "))
            nota2 = float(input(f"Digite a nota 2 de {nome}: "))
            media = (nota1 * 2 + nota2 * 3) / 5
            vetor.append((nome, media))
            print(f"Média ponderada de {nome}: {media}")
        print("Vetor de médias ponderadas:", vetor)
        
    elif op == 166:
        print("Você escolheu a opção 166")

        vetor = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor original:", vetor)
        for i in range(len(vetor)):
            if vetor[i] < 0:
                vetor[i] = 0
        print("Vetor com valores negativos substituídos por 0:", vetor)


    elif op == 167:
        print("Você escolheu a opção 167")

        vetor = []
        for i in range(5):
            valor = int(input(f"Digite o valor para a posição {i}: "))
            vetor.append(valor)
            print(f"Valor {valor} adicionado na posição {i}")
        print("Vetor:", vetor)
        contagem = {}
        for valor in vetor:
            if valor in contagem:
                contagem[valor] += 1
            else:
                contagem[valor] = 1
        moda = max(contagem, key=contagem.get)
        print("Moda:", moda)

    elif op == 168:
        print("Você escolheu a opção 168")

        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                 "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        print("Meses do ano:")
        for i in range(len(meses)):
            print(f"{i + 1} - {meses[i]}")
        mes = int(input("Digite o número do mês: "))
        if 1 <= mes <= 12:
            print(f"Mês escolhido: {meses[mes - 1]}")
        else:
            print("Mês inválido!")

    elif op == 169:
        print("Você escolheu a opção 169")

        vetor = []
        for i in range(5):
            string = input(f"Digite a string para a posição {i}: ")
            vetor.append(string)
            print(f"String '{string}' adicionada na posição {i}")
        print("Vetor de strings:", vetor)
        palindromos = []
        for string in vetor:
            if string == string[::-1]:
                palindromos.append(string)
        if palindromos:
            print("Palíndromos encontrados:", palindromos)

    elif op == 170:
        print("Você escolheu a opção 170")

        matriz = [[" " for _ in range(3)] for _ in range(3)]
        jogador = "X"
        for i in range(9):
            print("Matriz atual:")
            for linha in matriz:
                print("|".join(linha))
            linha = int(input(f"Jogador {jogador}, escolha a linha (0-2): "))
            coluna = int(input(f"Jogador {jogador}, escolha a coluna (0-2): "))
            if matriz[linha][coluna] == " ":
                matriz[linha][coluna] = jogador
                if jogador == "X":
                    jogador = "O"
                else:
                    jogador = "X"
            else:
                print("Posição já ocupada, tente novamente.")
        print("Jogo encerrado!")
        print("Matriz final:")
        for linha in matriz:
            print("|".join(linha))


    else:
        print("Opção inválida!")
    print(15 * "-+")
    print("0 = Sair")
    op = int(input("Esolha uma opção de 141 a 170: "))
    if op == 0:
        print("Saindo...")
        break