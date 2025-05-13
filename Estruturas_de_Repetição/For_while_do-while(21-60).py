print("ESTRUTURAS DE REPETIÇÃO")

op = int(input("Digite a sua opção:"))

while op != 0:
    print(30 * "-")
    print("0 = Sair")

    if op == 21:
        print("Você escolheu a opção 21")

        for i in range(1, 101):
            print(i)
        
    elif op == 22:
        print("Você escolheu a opção 22")

        arry = []
        for i in range(1, 51):
            arry.append(i)
            soma = sum(arry)
        print("A soma dos números de 1 a 50 é:", soma)

    elif op == 23:
        print("Você escolheu a opção 23")

        for i in range(1, 100, 5):
            print(i)

    elif op == 24:
        print("Você escolheu a opção 24")

        for i in range(1, 101):
            if i % 2 == 0:
                print(i)

    elif op == 25:
        print("Você escolheu a opção 25")

        cont_num = 0
        for i in range(1, 11):
            n = int(input("Digite um número:"))
            if n > 0:
                cont_num += 1
        print("Você digitou", cont_num, "números positivos.")

    elif op == 26:
        print("Você escolheu a opção 26")

        cont_num = 1
        for i in range(1, 11):
            print(f"1 X {i} é {cont_num}")
            print(f"2 X {i} é {cont_num * 2}")
            print(f"3 X {i} é {cont_num * 3}")
            print(f"4 X {i} é {cont_num * 4}")
            print(f"5 X {i} é {cont_num * 5}")
            print(f"6 X {i} é {cont_num * 6}")
            print(f"7 X {i} é {cont_num * 7}")
            print(f"8 X {i} é {cont_num * 8}")
            print(f"9 X {i} é {cont_num * 9}")
            print(f"10 X {i} é {cont_num * 10}")
            print("><><" * 10)
            cont_num += 1

    elif op == 27:
        print("Você escolheu a opção 27")

        n = int(input("Digite um número:"))
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        print(f"O fatorial de {n} é: {fatorial}")

    elif op == 28:
        print("Você escolheu a opção 28")

        n = int(input("Digite um número:"))
        print(f"Os divisores de {n} são:")
        for i in range(1, n + 1):
            if n % i == 0:
                print(i)

    elif op == 29:
        print("Você escolheu a opção 29")

        n = int(input("Digite um número:"))
        cont = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cont += 1
        if cont == 2:
            print(f"{n} é um número primo.")
        else:
            print(f"{n} não é um número primo.")

    elif op == 30:        
        print("Você escolheu a opção 30")

        n = int(input("Digite o número de termos da sequência de Fibonacci:"))
        a, b = 0, 1
        print("Sequência de Fibonacci:")
        for i in range(n):
            print(a)
            a, b = b, a + b
        
    elif op == 31:
        print("Você escolheu a opção 31")

        while True:
            n = int(input("Digite um número:"))
            if n == 0:
                break

    elif op == 32:
        print("Você escolheu a opção 32")

        cont_num = 0
        while True:
            n = int(input("Digite um número:"))
            cont_num += n
            print("A soma dos números digitados é:", cont_num)
            if n == -1:
                break
                
    elif op == 33:
        print("Você escolheu a opção 33")

        pares = []
        for i in range(1, 10):
            n = int(input("Digite um número:"))
            if n % 2 == 0:
                pares.append(n)
        print("Os números pares digitados foram:", pares)
    
    elif op == 34:
        print("Você escolheu a opção 34")

        while True:
            n = int(input("Digite um número:"))
            if n < 0 or n > 10:
                print("Valor invalido!")
                break

    elif op == 35:
        print("Você escolheu a opção 35")

        saldo = 1000
        print(f"Seu saldo é: {saldo}")
        for i in range(1, 11):
            saldo -= 100
            print(f"Seu saldo é: {saldo}")

    elif op == 36:
        print("Você escolheu a opção 36")

        n = int(input("Quantos números você quer digitar?"))
        media = n / n
        print("A média é:", media)

    elif op == 37:
        print("Você escolheu a opção 37")

        senha = "1234"
        while True:
            senha_digitada = input("Digite a senha:")
            if senha_digitada == senha:
                print("Acesso permitido!")
                break
            else:
                print("Senha incorreta! Tente novamente.")
    
    elif op == 38:
        print("Você escolheu a opção 38")

        for i in range(100, -1, -1):
            if i == 0:
                break
            print(i)

    elif op == 39:
        print("Você escolheu a opção 39")

        for i in range(10, -1, -1):
            print(f"{i} segundos restantes")

    elif op == 40:
        print("Você escolheu a opção 40")

        tentativas = 2
        senha = "1234"
        for i in range(tentativas):
            senha_digitada = input("Digite a senha:")
            if senha_digitada == senha:
                print("Acesso permitido!")
                break
            else:
                print("Senha incorreta! Tente novamente.")
        
    elif op == 41:
        print("Você escolheu a opção 41")

        soma = 0
        for i in range(1, 101, 2):
            soma += i
        print("A soma dos números ímpares de 1 a 100 é:", soma)

    elif op == 42:
        print("Você escolheu a opção 42")

        n = int(input("Digite um número:"))
        for i in range(1, n, 2):
                print(i)

    elif op == 43:
        print("Você escolheu a opção 43")

        for i in range(24):
            for j in range(60):
                print(f"{i:02}:{j:02}")

    elif op == 44:
        import random
        print("Você escolheu a opção 44")

        n = int(input("Digite um número:"))
        i = 2
        while i <= n:
            print(i)
            i = i * 2

    elif op == 45:
        print("Você escolheu a opção 45")

        for i in random.randint(1, 10):
            n = int(input("Escolha um número de 0 A 10:"))
            if n == i:
                print("Você acertou!")
                break
            else:
                print("Você errou! Tente novamente.")

    elif op == 46 and op == 47:
        print("Você escolheu a opção 46/47")

        maior = 0
        menor = 0
        for i in range(1, 11):
            n = int(input("Digite um número:"))
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        print("O maior número é:", maior)
        print("O menor número é:", menor)

    elif op == 48:
        print("Você escolheu a opção 48")

        notas = []
        cont_num = 1
        for i in range(1, 6):
            n = float(input(f"Digite a nota:{cont_num}°:"))
            notas.append(n)
            cont_num += 1
        media = sum(notas) / 5
        print("A média das notas é:", media)

    elif op == 49:
        print("Você escolheu a opção 49")

        divida = 1000
        while divida > 0:
            valor_pago_boleto = float(input("Digite o valor do boleto:"))
            divida -= valor_pago_boleto
            print(f"Valor restante da dívida: {divida}")

    elif op == 50 and op == 58:
        print("Você escolheu a opção 50/58")

        n1 = int (input('digite um numero:'))
        n2 = int (input(' digite outro numero:'))
        op = 0
        while op != 5:
            print('''    
            [1] somar
            [2] multiplicar
            [3] maior 
            [4] novos numeros 
            [5] sair''')
            op = int(input('>>>>>qual é a sua opção?<<<<<<'))
            if op == 1:
                s = n1 + n2
                print(f'A soma entre {n1} + {n2} é {s}')
            elif op == 2:
                p = n1 * n2
                print(f'o resutado de  {n1} X {n2} é {p}')
            elif op == 3:
                if n1 > n2:
                    maior = n1
                else:
                    maior = n2
                    print(f'entre {n1} e {n2} o maior valor é {maior}')
            elif op == 4:
                print('informe os numeros nova mente:')
                n1 = int(input('digite um numero:'))
                n2 = int(input('digite outro numero:'))
            elif op == 5:
                print('finalizando...')
            else:
                print('opção inválida. tente novamente')
            print('=-=' * 10)
            print('fim do programa! volte sempre!')

            
    elif op == 51:
        print("Você escolheu a opção 51")

        lt = float(input("Digite a quantidade de litros:"))
        valor_tt = lt * 6.30
        print(f"O valor total a ser pago é: {valor_tt}")

    elif op == 52:
        print("Você escolheu a opção 52")

        n = int(input("Digite um número:"))
        print("Sequência de Collatz:")
        while n != 1:
            print(n, end=" ")
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        print(1)

    elif op == 53:
        print("Você escolheu a opção 53")

        frase = input("Digite uma frase:")
        cont = 0
        for letra in frase:
            if letra == "a":
                cont += 1
        print(f"A letra 'a' aparece {cont} vezes na frase.")

    elif op == 54:
        print("Você escolheu a opção 54")

        a = int(input("Digite o primeiro número:"))
        b = int(input("Digite o segundo número:"))
        while b != 0:
            a, b = b, a % b
        print(f"O MDC é: {a}")

    elif op == 55:
        print("Você escolheu a opção 55")

        n = int(input("Digite um número:"))
        p = int(input("Digite a potência:"))
        resultado = 1
        for i in range(p):
            resultado *= n
        print(f"{n} elevado a {p} é: {resultado}")

    elif op == 56:
        print("Você escolheu a opção 56")

        n = int(input("Digite o número de linhas que você quer:"))
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()
    
    elif op == 57:
        print("Você escolheu a opção 57")

        print("Candidatos:")
        print("1 - Candidato Bolsonaro")
        print("2 - Candidato Lula")
        print("3 - Candidato Ciro")
        print("0 - Encerrar votação")
        votos = [0, 0, 0]
        while True:
            voto = int(input("Digite o número do candidato:"))
            if voto == 0:
                break
            elif 1 <= voto <= 3:
                votos[voto - 1] += 1
            else:
                print("Voto inválido!")
        print("Resultado da votação:")

        print(f"Candidato A: {votos[0]} votos")
        print(f"Candidato B: {votos[1]} votos")
        print(f"Candidato C: {votos[2]} votos")

    elif op == 59:
        print("Você escolheu a opção 58")

        total = 0
        while True:
            preco = float(input("Digite o preço do produto (0 para sair):"))
            if preco == 0:
                break
            total += preco
        print(f"O total a ser pago é: {total}")

    elif op == 60:
        print("Você escolheu a opção 60")

        temperatura = 0
        while True:
            temperatura = int(input("Digite a temperatura do forno:"))
            if temperatura < 0:
                print("Forno desligado!")
                break
            elif temperatura > 200:
                print("Temperatura muito alta!")
            else:
                print(f"Temperatura do forno: {temperatura}°C")
    else:
        print("Opção inválida!")
    print(30 * "-")

           
    op = int(input("Digite a sua opção:"))