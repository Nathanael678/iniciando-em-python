from Funções import*

print("PROCEDIMENTOS E MODULARIZAÇÃO")

op = int(input("Digite qual opção você quer:"))

while op != 0:
    print(15 * "-+")
    print("0 = Sair")

    if op == 101:
        print("Você escolheu a opção 101")
        n1 = int(input("Digite o primeiro número:"))
        n2 = int(input("Digite o segundo número:"))
        soma(n1, n2)

    elif op == 102:
        print("Você escolheu a opção 102")

        n = int(input("Digite o número:"))
        print(f"O fatorial de {n} é: {fatorial(n)}")

    elif op == 103:
        print("Você escolheu a opção 103")

        n = int(input("Digite o número:"))
        if primo(n):
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo")

    elif op == 104:
        print("Você escolheu a opção 104")

        n1 = float(input("Digite a primeira nota:"))
        n2 = float(input("Digite a segunda nota:"))
        n3 = float(input("Digite a terceira nota:"))
        print(f"A média é: {notas(n1, n2, n3)}")

    elif op == 105:
        print("Você escolheu a opção 105")

        n1 = float(input("Digite o valor em Celsius:"))
        print(f"O valor em Fahrenheit é: {Celsius_para_Fahrenheit(n1)}")

    elif op == 106:
        print("Você escolheu a opção 106")

        n = int(input("Digite o número:"))
        print(f"{n} é {impar_ou_par(n)}")

    elif op == 107:
        print("Você escolheu a opção 107")

        n = str(input("Digite uma palavra:"))
        quantidade = numero_de_letras(n)
        print(f"O número de letras é: {quantidade}")

    elif op == 108:
        print("Você escolheu a opção 108")

        n1 = int(input("Digite o primeiro número:"))
        n2 = int(input("Digite o segundo número:"))
        n3 = int(input("Digite o terceiro número:"))
        print(f"O maior número é: {maior_de_tres(n1, n2, n3)}")

    elif op == 109:
        print("Você escolheu a opção 109")

        raio = float(input("Digite o raio do círculo:"))
        print(f"A área do círculo é: {area_circulo(raio)}")

    elif op == 110:
        print("Você escolheu a opção 110")

        name = str(input("Digite seu nome:"))
        print(bem_vindo(name))

    elif op == 111:
        print("Você escolheu a opção 111")

        n = int(input("Digite um número:"))
        print(f"O valor absoluto de {n} é: {valor_absoluto(n)}")

    elif op == 112:
        print("Você escolheu a opção 112")

        base = int(input("Digite a base:"))
        expoente = int(input("Digite o expoente:"))
        print(f"{base} elevado a {expoente} é: {potencia(base, expoente)}")

    elif op == 113:
        print("Você escolheu a opção 113")

        tabuada(n=int(input("Digite o número:")))

    elif op == 114:
        print("Você escolheu a opção 114")

        array = []
        for i in range(5):
            n = int(input("Digite o número:"))
            array.append(n)
        print(f"O menor número é: {menor_da_lista(array)}")

    elif op == 115:
        print("Você escolheu a opção 115")

        print("Escolha de 1 a 5:")
        i = int(input("Digite o índice:"))
        indice_da_lista([1, 2, 3, 4, 5])

    elif op == 116:
        print("Você escolheu a opção 116")

        s = str(input("Digite uma palavra:"))
        print(f"A palavra invertida é: {inverte_string(s)}")

    elif op == 117:
        print("Você escolheu a opção 117")

        n1 = int(input("Digite o primeiro número:"))
        n2 = int(input("Digite o segundo número:"))

        if mutiplo_de_outro(n1, n2):
            print(f"{n1} é múltiplo de {n2}")
        else:
            print(f"{n1} não é múltiplo de {n2}")
    
    elif op == 118:
        print("Você escolheu a opção 118")

        nome = str(input("Digite seu nome:"))
        largura = int(input("Digite a largura:"))
        altura = int(input("Digite a altura:"))
        caixa_com_nome(largura, altura, nome)

    elif op == 119:
        print("Você escolheu a opção 119")

        calculadora()

    elif op == 120:
        print("Você escolheu a opção 120")

        senha()
        
    elif op == 121:
        print("Você escolheu a opção 121")

        letra = str(input("Digite uma letra:"))
        print(f"A letra {letra} é uma {vogal_consoante(letra)}")
    
    elif op == 122:
        print("Você escolheu a opção 122")

        s = str(input("Digite uma palavra:"))
        print(f"A palavra {s} tem {quatidade_de_vogais(s)}")

    elif op == 123:
        print("Você escolheu a opção 123")

        n = int(input("Digite o número de elementos do vetor:"))
        vetor = []
        for i in range(n):
            elemento = int(input(f"Digite o elemento {i + 1}: "))
            vetor.append(elemento)
        print(f"Os números pares no vetor são: {numeros_pares_vetor(vetor)}")

    elif op == 124:
        print("Você escolheu a opção 124")

        matriz = []
        for i in range(3):
            linha = []
            for j in range(3):
                elemento = int(input(f"Digite o elemento [{i}][{j}]: "))
                linha.append(elemento)
            matriz.append(linha)
        print(f"A média da matriz é: {media_matriz(matriz)}")

    elif op == 125:
        print("Você escolheu a opção 125")

        cpf = str(input("Digite o CPF:"))
        if validar_cpf(cpf):
            print(f"{cpf} é um CPF válido")
        else:
            print(f"{cpf} não é um CPF válido")

    elif op == 126:
        print("Você escolheu a opção 126")

        n = int(input("Digite o número de elementos do vetor:"))
        vetor = []
        for i in range(n):
            elemento = int(input(f"Digite o elemento {i + 1}: "))
            vetor.append(elemento)
        print(f"O vetor ordenado é: {vetor_bubble_sort(vetor)}")

    elif op == 127:
        print("Você escolheu a opção 127")

        a = int(input("Digite o primeiro número:"))
        b = int(input("Digite o segundo número:"))
        print(f"O MDC de {a} e {b} é: {caucular_mdc(a, b)}")
        a, b = b, a % b
        while b != 0:
            a, b = b, a % b
        print(f"O MDC de {a} e {b} é: {a}")

    elif op == 128:
        print("Você escolheu a opção 128")

        a = int(input("Digite o primeiro número:"))
        b = int(input("Digite o segundo número:"))
        print(f"O MMC de {a} e {b} é: {caulcular_mmc(a, b)}")
        a, b = b, a % b
        while b != 0:
            a, b = b, a % b
        print(f"O MMC de {a} e {b} é: {a}")

    elif op == 129:
        print("Você escolheu a opção 129")

        s = str(input("Digite uma frase:"))
        print(f"A frase tem {numero_de_palavras(s)} numero_de_palavras")

    elif op == 130:
        print("Você escolheu a opção 130")

        tamanho = int(input("Digite o tamanho da senha:"))
        senha = senha_aleatoria(tamanho)
        print(f"A senha aleatória gerada é: {senha}")

    elif op == 131:
        print("Você escolheu a opção 131")

        print("A atividade em se já é isso!!!")

    elif op == 132:
        print("Você escolheu a opção 132")

        horas = int(input("Digite as horas:"))
        total_segundos = converte_horas_em_minutos_segundos(horas)
        print(f"O total de segundos é: {total_segundos}")

    elif op == 133:
        print("Você escolheu a opção 133")

        s = str(input("Digite uma frase:"))
        print(f"A frase sem espaços é: {remover_espacos(s)}")

    elif op == 134:
        print("Você escolheo a opção 134")

        numero = int(input("Digite um número:"))
        print(f"A soma dos dígitos de {numero} é: {soma_digitos(numero)}")

    elif op == 135:
        print("Você escolheu a opção 135")

        altura = int(input("Digite a altura da árvore:"))
        print("A árvore desenhada é:")
        for i in range(altura):
            print(" " * (altura - i - 1) + "*" * (2 * i + 1))
        print(" " * (altura - 1) + "|")
        desenha_uma_arvore(altura)
    
    elif op == 136:
        print("Você escolheu a opção 136")

        s = str(input("Digite uma palavra:"))
        letras = letras_repetidas(s)
        print("As letras repetidas são:")
        for letra, quantidade in letras.items():
            if quantidade > 1:
                print(f"{letra}: {quantidade} vezes")

    elif op == 137:
        print("Você escolheu a opção 137")

        s = str(input("Digite uma palavra:"))
        s_embaralhada = embaralhar_string(s)
        print(f"A palavra embaralhada é: {s_embaralhada}")

    elif op == 138:
        print("Você escolheu a opção 138")

        s = str(input("Digite uma palavra:"))
        print(f"A palavra com vogais substituídas por asterisco é: {substituir_vogais_por_asterisco(s)}")

    elif op == 139:
        print("Você escolheu a opção 139")

        nome = str(input("Digite seu nome:"))
        iniciais = iniciais_do_nome(nome)
        print(f"As iniciais do seu nome são: {iniciais}")

    elif op == 140:
        print("Você escolheu a opção 140")

        data = str(input("Digite a data no formato dd/mm/aaaa:"))
        if data_valida(data):
            print(f"A data {data} é válida")
        else:
            print(f"A data {data} não é válida")

    elif op == 141:
        print("Você escolheu a opção 141")

        


    op = int(input("Digite qual opção você quer:"))
    if op == 0:
        print("Saindo...")
        break