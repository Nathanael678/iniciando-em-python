print("CONDICIONAIS E LÓGICAS COMPOSTAS")

op = int(input("Digite a sua opção:"))

while op != 0:
    print(30 * "-")
    print("0 = Sair")

    if op == 61:
        print("Você escolheu a opção 61")

        n = int(input("Digite um número: "))
        if n % 2 == 0:
            print("O número é par")
        else:
            print("O número é ímpar")
    
    elif op == 62:
        print("Você escolheu a opção 62")

        n = int(input("Digite um número: "))
        if n % 3 == 0:
            print("O número é múltiplo de 3")
        else:
            print("O número não é múltiplo de 3")

    elif op == 63:
        print("Você escolheu a opção 63")

        alunos = []
        notas = []

        print(">>>ATIVIDADE MÉDIA DOS ALUNOS!/ TRABALHO DE LÓGICA<<<")
        qtdaluno = int(input("Digite a quantidade de alunos:"))
        qtdnota = int(input("Digite a quantidade de notas por aluno:"))
        print("=+=+" * 15)

        cont_aluno = 1
        for i in range(qtdaluno):
            nome_aluno = str(input(f"Digite o nome do {cont_aluno}° aluno:"))
            alunos.append(nome_aluno)
            cont_aluno += 1
            print("=+=+" * 15)

            soma_nota = 0
            cont_nota = 1
            for i in range(qtdnota):
                nota = float(input(f"Digite a {cont_nota}° nota do aluno {nome_aluno}:"))
                soma_nota += nota
                cont_nota += 1
            print("=+=+" * 15)   
            
            media = soma_nota / qtdnota
            notas.append(media)

        indice_aluno = 0
        for i in range(qtdaluno):
            print(f"A média do aluno {alunos[indice_aluno]} é: {notas[indice_aluno]}")
            situacao = notas[indice_aluno]
            indice_aluno += 1
            if situacao > 6:
                print("Aprovado")
            elif situacao == 5:
                print("Recuperação")
            else:
                print("Reprovado")
            print("=+=+" * 15)
            print("")

    elif op == 64:
        print("Você escolheu a opção 64")

        ano = int(input("Digite um ano: "))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"{ano} é um ano bissexto")
        else:
            print(f"{ano} não é um ano bissexto")

    elif op == 65:
        print("Você escolheu a opção 65")

        senha = str(input("Digite uma senha: "))
        if len(senha) >= 6:
            print("Senha válida")
        else:
            print("Senha inválida")

    elif op == 66:
        print("Você escolheu a opção 66")

        #clacifique uma idade criaça, adolescente, adulto e idoso
        idade = int(input("Digite a sua idade: "))
        if idade < 12:
            print("Criança")
        elif idade >= 12 and idade < 18:
            print("Adolescente")
        elif idade >= 18 and idade < 60:
            print("Adulto")
        else:
            print("Idoso")

    elif op == 67:
        print("Você escolhei a opção 67")

        idade = int(input("Digite a sua idade: "))
        peso = float(input("Digite o seu peso: "))
        if idade >= 18 and peso >= 50:
            print("Você pode doar sangue")
        else:
            print("Você não pode doar sangue")

    elif op == 68:
        print("Você escolheu a opção 68")

        cor = str(input("Digite a cor do semáforo (vermelho, amarelo ou verde): "))
        if cor == "vermelho":
            print("Pare")
        elif cor == "amarelo":
            print("Atenção")
        elif cor == "verde":
            print("Siga")

    elif op == 69:
        print("Você escolheu a opção 69")

        #calacifique um triângulo com base em seus lados
        lado1 = float(input("Digite o primeiro lado do triângulo: "))
        lado2 = float(input("Digite o segundo lado do triângulo: "))
        lado3 = float(input("Digite o terceiro lado do triângulo: "))
        if lado1 == lado2 and lado2 == lado3:
            print("Triângulo equilátero")
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            print("Triângulo isósceles")
        else:
            print("Triângulo escaleno")

    elif op == 70:
        print("Você escolheu a opção 70")

        login = str(input("Digite o seu login: "))
        senha = str(input("Digite a sua senha: ")) 
        if login == "admin" and senha == "1234":
            print("Acesso permitido")
        else:
            print("Acesso negado")
        
    elif op == 71:
        print("Você escolheu a opção 71")

        valor_da_compra = float(input("Digite o valor da compra: "))
        cupon = str(input("Digite o número do cupom: "))
        if cupon == "1234":
            valor_final = valor_da_compra - 10
            print(f"Valor final com desconto:R${valor_final}")
        else:
            print(f"Valor final sem desconto:R${valor_da_compra}")

    elif op == 72:
        print("Você escolheu a opção 72")

        numero = float(input("Digite um número: "))
        if numero % 1 == 0:
            print("O número é inteiro")
        else:
            print("O número é decimal")

    elif op == 73:
        print("Você escolheu a opção 73")

        string = str(input("Digite uma string: "))
        if "admin" in string:
            print("A string contém a palavra admin")
        else:
            print("A string não contém a palavra admin")

    elif op == 74:
        print("Você escolheu a opção 74")

        #verificar se o a luno tem frequencia suficiente
        nome_aluno = str(input("Digite o nome do aluno: "))
        frequencia = int(input("Digite a frequência do aluno: "))
        if frequencia >= 75:
            print(f"{nome_aluno} tem frequência suficiente")
        else:
            print(f"{nome_aluno} não tem frequência suficiente")
    
    elif op == 75:
        print("Você escolheu a opção 75")

        #calcular a comição de um vendedor com base em suas vendas
        vendas = float(input("Digite o valor das vendas: "))
        comissao = vendas * 0.1
        print(f"A comissão do vendedor é: R${comissao}")
    
    elif op == 76:
        print("Você escolheu a opção 76")

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        if num1 > num2 and num1 > num3:
            print(f"O maior número é: {num1}")
        elif num2 > num1 and num2 > num3:
            print(f"O maior número é: {num2}")
        else:
            print(f"O maior número é: {num3}")

    elif op == 77:
        print("Você escolheu a opção 77")

        lado1 = float(input("Digite o primeiro lado do triângulo: "))
        lado2 = float(input("Digite o segundo lado do triângulo: "))
        lado3 = float(input("Digite o terceiro lado do triângulo: "))
        if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
            print("Os lados formam um triângulo")
        else:
            print("Os lados não formam um triângulo")

    elif op == 78:
        print("Você escolheu a opção 78")

        #simule um caixa eletrônico noatas 100, 50, 20, 10, 5 e 2, osne a pessoa vai digitar o valor que quer sacar e o caixa vai falar quantas notas de cada valor vai dar
        print("Bem-vindo ao Caixa Eletrônico!")
        valor = int(input("Digite o valor que deseja sacar: "))
    
        notas = [100, 50, 20, 10, 5, 2]
        for nota in notas:
            quantidade = valor // nota
            if quantidade > 0:
                print(f"{quantidade} nota(s) de R$ {nota}")
                valor %= nota

    elif op == 79:
        print("Você escolheu a opção 79")

        print("Bem-vindo ao conversor de moeda!")
        print("1 - Dólar para Real")
        print("2 - Real para Dólar")
        print("3 - Euro para Real")
        print("4 - Real para Euro")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        valor = float(input("Digite o valor a ser convertido: "))

        if opcao == 1:
            taxa = 5.25
            valor_convertido = valor * taxa
            print(f"{valor} Dólares = {valor_convertido} Reais")
        elif opcao == 2:
            taxa = 0.19
            valor_convertido = valor * taxa
            print(f"{valor} Reais = {valor_convertido} Dólares")
        elif opcao == 3:
            taxa = 6.20
            valor_convertido = valor * taxa
            print(f"{valor} Euros = {valor_convertido} Reais")
        elif opcao == 4:
            taxa = 0.16
            valor_convertido = valor * taxa
            print(f"{valor} Reais = {valor_convertido} Euros")
        elif opcao == 0:
            print("Saindo do conversor de moeda...")
    
    elif op == 80:
        print("Você escolheu a opção 80")

        #simule um alarme baseado no horario
        hora = int(input("Digite a hora (0-23): "))
        minuto = int(input("Digite o minuto (0-59): "))
        segundo = int(input("Digite o segundo (0-59): "))
        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59:
            print("Horário inválido")
        else:
            print(f"Alarme definido para {hora:02d}:{minuto:02d}:{segundo:02d}")
    
    elif op == 81:
        print("Você escolheu a opção 81")

        num = float(input("Digite um número: "))
        limite_inferior = float(input("Digite o limite inferior: "))
        limite_superior = float(input("Digite o limite superior: "))
        if limite_inferior <= num <= limite_superior:
            print(f"{num} está entre {limite_inferior} e {limite_superior}")
        else:
            print(f"{num} não está entre {limite_inferior} e {limite_superior}")

    elif op == 82:
        print("Você escolheu a opção 82")

        print("Calculadora")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif opcao == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif opcao == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif opcao == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Divisão por zero não é permitida")
        elif opcao == 0:
            print("Saindo da calculadora...")

    elif op == 83:
        print("Você escolheu a opção 83")

        cpf = str(input("Digite o CPF (apenas números): "))
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido")
        else:
            print("CPF válido")

    elif op == 84:
        print("Você escolheu a opção 84")

        nota = float(input("Digite a nota (0 a 10): "))
        if nota >= 9:
            print("A")
        elif nota >= 8:
            print("B")
        elif nota >= 7:
            print("C")
        elif nota >= 6:
            print("D")
        elif nota >= 5:
            print("E")
        else:
            print("F")

    elif op == 85:
        print("Você escolheu a opção 85")

        palavra = str(input("Digite uma palavra: "))
        if palavra == palavra[::-1]:
            print(f"{palavra} é um palíndromo")
        else:
            print(f"{palavra} não é um palíndromo")

    elif op == 86:
        print("Você escolheu a opção 86")

        lista = [1, 2, 3, 4, 5]
        numero = int(input("Digite um número: "))
        if numero in lista:
            print(f"{numero} está na lista")
        else:
            print(f"{numero} não está na lista")
    
    elif op == 87:
        print("Você escolheu a opção 87")

        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        if nota1 <= nota2 and nota1 <= nota3:
            media = (nota2 + nota3) / 2
        elif nota2 <= nota1 and nota2 <= nota3:
            media = (nota1 + nota3) / 2
        else:
            media = (nota1 + nota2) / 2
        print(f"A média das notas é: {media}")

    elif op == 88:
        print("Você escolheu a opção 88")

        idade = int(input("Digite a sua idade: "))
        if idade >= 18:
            print("Você pode entrar na festa")
        else:
            print("Você não pode entrar na festa")

    elif op == 89:
        print("Você escolheu a opção 89")

        sabores = ["Calabresa", "Frango", "Margherita", "Portuguesa"]
        print("Sabores disponíveis:")
        for i, sabor in enumerate(sabores, start=1):
            print(f"{i} - {sabor}")
        escolha = int(input("Escolha o sabor da pizza (1-4): "))
        if 1 <= escolha <= len(sabores):
            print(f"Você escolheu a pizza de {sabores[escolha - 1]}")
        else:
            print("Opção inválida")

    elif op == 90:
        print("Você escolheu a opção 90")

        #leia dois horarios e diga qual é o maior
        hora1 = int(input("Digite a primeira hora (0-23): "))
        minuto1 = int(input("Digite o primeiro minuto (0-59): "))
        hora2 = int(input("Digite a segunda hora (0-23): "))
        minuto2 = int(input("Digite o segundo minuto (0-59): "))
        
        if (hora1 < 0 or hora1 > 23 or minuto1 < 0 or minuto1 > 59 or
            hora2 < 0 or hora2 > 23 or minuto2 < 0 or minuto2 > 59):
            print("Horário inválido")
        else:
            if (hora1 > hora2) or (hora1 == hora2 and minuto1 > minuto2):
                print(f"{hora1:02d}:{minuto1:02d} é maior que {hora2:02d}:{minuto2:02d}")
            elif (hora1 < hora2) or (hora1 == hora2 and minuto1 < minuto2):
                print(f"{hora2:02d}:{minuto2:02d} é maior que {hora1:02d}:{minuto1:02d}")
            else:
                print("Os horários são iguais")

    elif op == 91:
        print("Você escolheu a opção 91")

        hora1 = int(input("Digite a primeira hora (0-23): "))
        minuto1 = int(input("Digite o primeiro minuto (0-59): "))
        hora2 = int(input("Digite a segunda hora (0-23): "))
        minuto2 = int(input("Digite o segundo minuto (0-59): "))

        if (hora1 < 0 or hora1 > 23 or minuto1 < 0 or minuto1 > 59 or
            hora2 < 0 or hora2 > 23 or minuto2 < 0 or minuto2 > 59):
            print("Horário inválido")
        
        print("Diferença entre os horários:")
        if hora1 > hora2 or (hora1 == hora2 and minuto1 > minuto2):
            diferenca_hora = hora1 - hora2
            diferenca_minuto = minuto1 - minuto2
            print(f"{diferenca_hora} horas e {diferenca_minuto} minutos")
        elif hora1 < hora2 or (hora1 == hora2 and minuto1 < minuto2):
            diferenca_hora = hora2 - hora1
            diferenca_minuto = minuto2 - minuto1
            print(f"{diferenca_hora} horas e {diferenca_minuto} minutos")

        elif hora1 == hora2 and minuto1 == minuto2:
            print("Os horários são iguais")

        elif hora1 == hora2 and minuto1 > minuto2:
            diferenca_hora = 0
            diferenca_minuto = minuto1 - minuto2
            print(f"{diferenca_hora} horas e {diferenca_minuto} minutos")

        else:
            diferenca_hora = hora2 - hora1
            diferenca_minuto = minuto2 - minuto1
            print(f"{diferenca_hora} horas e {diferenca_minuto} minutos")

    elif op == 92:
        print("Você escolheu a opção 92")

        numero = int(input("Digite um número: "))
        soma_divisores = 0

        for i in range(1, numero):
            if numero % i == 0:
                soma_divisores += i

        if soma_divisores == numero:
            print(f"{numero} é um número perfeito!")
        else:
            print(f"{numero} não é um número perfeito.")

    elif op == 93:
        print("Você escolheu a opção 93")

        distancia = float(input("Digite a distância em km: "))
        velocidade = float(input("Digite a velocidade em km/h: "))
        if velocidade <= 0:
            print("Velocidade inválida")
        else:
            tempo = distancia / velocidade
            horas = int(tempo)
            minutos = int((tempo - horas) * 60)
            print(f"Tempo de viagem: {horas} horas e {minutos} minutos")

    elif op == 94:
        print("Você escolheu a opção 94")

        idade = int(input("Digite a sua idade: "))
        if idade >= 18:
            print("Você pode tirar a CNH")
        else:
            print("Você não pode tirar a CNH")

    elif op == 95:
        print("Você escolheu a opção 95")

        import random
        premio = random.randint(1, 10)
        aposta = int(input("Digite o número da sua aposta (1-10): "))
        if aposta < 1 or aposta > 10:
            print("Aposta inválida")
        else:
            if aposta == premio:
                print("Parabéns! Você ganhou o prêmio!")
            else:
                print(f"Você perdeu. O prêmio era {premio}")

    elif op == 96:
        print("Você escolheu a opção 96")

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        num3 = int(input("Digite o terceiro número: "))
        if num1 > num2 and num1 > num3:
            maior = num1
        elif num2 > num1 and num2 > num3:
            maior = num2
        else:
            maior = num3

    elif op == 97:
        print("Você escolheu a opção 97")

        numero = float(input("Digite um número: "))
        if numero > 0:
            print("O número é positivo")
        elif numero < 0:
            print("O número é negativo")
        else:
            print("O número é zero")

    elif op == 98:
        print("Você escolheu a opção 98")

        perguntas = [
            {
                "pergunta": "Qual a capital do Brasil?",
                "alternativas": ["1. Brasília", "2. São Paulo", "3. Rio de Janeiro", "4. Salvador"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual a capital da França?",
                "alternativas": ["1. Paris", "2. Londres", "3. Roma", "4. Madri"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual a capital da Itália?",
                "alternativas": ["1. Roma", "2. Paris", "3. Berlim", "4. Lisboa"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual a capital da Alemanha?",
                "alternativas": ["1. Berlim", "2. Viena", "3. Bruxelas", "4. Amsterdã"],
                "resposta_correta": 1
            },
            {
                "pergunta": "Qual a capital da Espanha?",
                "alternativas": ["1. Madri", "2. Barcelona", "3. Sevilha", "4. Valência"],
                "resposta_correta": 1
            }
        ]
        acertos = 0
        for pergunta in perguntas:
            print(pergunta["pergunta"])
            for alternativa in pergunta["alternativas"]:
                print(alternativa)
            resposta = int(input("Digite o número da sua resposta: "))
            if resposta == pergunta["resposta_correta"]:
                acertos += 1
                print("Resposta correta!")
            else:
                print("Resposta incorreta.")
        print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")

    elif op == 99:
        print("Você escolheu a opção 99")

        numero = int(input("Digite um número: "))
        soma = 0
        temp = numero
        while temp > 0:
            digito = temp % 10
            soma += digito ** 3
            temp //= 10
        if soma == numero:
            print(f"{numero} é um número de Armstrong")

        elif soma != numero:
            print(f"{numero} não é um número de Armstrong")

        else:
            print("Número inválido")

    elif op == 100:
        print("Você escolheu a opção 100")

        salario = float(input("Digite o seu salário: "))
        if salario <= 1903.98:
            print("Isento de imposto de renda")
        elif salario <= 2826.65:
            imposto = salario * 0.075 - 142.80
            print(f"Imposto de renda: R${imposto:.2f}")
        elif salario <= 3751.05:
            imposto = salario * 0.15 - 354.80
            print(f"Imposto de renda: R${imposto:.2f}")
        elif salario <= 4664.68:
            imposto = salario * 0.225 - 636.13
            print(f"Imposto de renda: R${imposto:.2f}")
        else:
            imposto = salario * 0.275 - 869.36
            print(f"Imposto de renda: R${imposto:.2f}")        

    else:
        print("Opção inválida")
    print(15 * "_-_-")
    print("0 = Sair")
    op = int(input("Digite a sua opção:"))