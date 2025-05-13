print("fUNDAMENTOS E ALGORITMOS")

op = int(input("Digite qual opção você quer:"))

while op != 0:
    print(30 * "-")
    print("0 = Sair")
    

    if op == 1:
        print("Você escolheu a opção 1")

        n1 = int(input("Digite o primeiro número:"))
        n2 = int(input("Digite o segundo número:"))

        if n1 > n2:
            print("O maior número é:", n1)
        elif n2 > n1:
            print("O maior nùmero é:", n2)
        else:
            print("Os dois são iguais!")

    elif op == 2:
        print("Você escolheu a opção 2")

        valor_hora = float(input("Digite o valor da hora:"))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas:"))

        salario = valor_hora * horas_trabalhadas
        print("O salário é:", salario)
    
    elif op == 3:
        print("Você escolheu a opção 3")

        Temp_C = float(input("Digite a temperatura em Celsius:"))
        Temp_F = (Temp_C * 9/5) + 32
        print("A temperatura em Fahrenheit é:", Temp_F)

    elif op == 4:
        print("Você escolheu a opção 4")

        n1 = int(input("Digite um número:"))
        dobro = n1 * 2
        print(f"O dobro de {n1} é: {dobro}")

    elif op == 5:
        print("Você escolheu a opção 5")

        n1 = int(input("Digite um número:"))
        quadrado = n1 ** 2
        print(f"O quadrado de {n1} é: {quadrado}")

    elif op == 6:
        print("Você escolheu a opção 6")

        n1 = int(input("Digite um número:"))
        n2 = int(input("Digite outro número:"))
        soma = n1 + n2 
        print(f"A soma de {n1} e {n2} é: {soma}")

    elif op == 7:
        print("Você escolheu a opção 7")

        n1 = int(input("Digite a sua idade:"))
        ano_dias = 365
        idade_dias = n1 * ano_dias
        print(f"A sua idade em dias é: {idade_dias}")

    elif op == 8:
        print("Você escolheu a opção 8") 

        v1 = int(input("Digite o primeiro valor:"))
        v2 = int(input("Digite o segundo valor:"))
        troca = v1
        v1 = v2
        v2 = troca
        print(f"Valor 1: {v1} e Valor 2: {v2}")

    elif op == 9:
        print("Você escolheu a opção 9")

        n1 = int(input("Digite um número:"))

        if n1 > 0:
            print("O número é positivo")
        elif n1 < 0:
            print("O número é negativo")
        else:
            print("O número é zero por tanto é neutro")

    elif op == 10:
        print("Você escolheu a opação 10")

        n1 = float(input("Digite quantas horas foram:"))
        valor_hora = 1.00
        valor_total = n1 * valor_hora
        print(f"O valor total é: {valor_total}")

    elif op == 11:
        print("Você escolheu a opção 11")

        n1 = int(input("Digite um número:"))
        n2 = int(input("Digite outro número:"))
        n3 = int(input("Digite mais um número:"))

        media = (n1 + n2 + n3) / 3
        print(f"A média é: {media}")

    elif op == 12:
        print("Você escolheu a opção 12")

        n1 = float(input("Digite um valor:"))
        dolar = 5.00
        valor_dolar = n1 * dolar
        print(f"O valor em dólar é: {valor_dolar}")

    elif op == 13:
        print("Você escolheu a opção 13")

        km = float(input("Digite a distância em km:"))
        consumo = float(input("Digite o consumo em litros:"))
        media = km / consumo
        print(f"A média de consumo é: {media} km/l")

    elif op == 14:
        print("Você escolheu a opção 14")

        peso = float(input("Digite o peso:"))
        altura = float(input("Digite a altura:"))
        imc = peso / (altura ** 2)
        print(f"O IMC é: {imc}")

        if imc < 18.5:
            print("Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            print("Peso normal")
        elif 25 <= imc < 29.9:
            print("Sobrepeso")
        elif 30 <= imc < 34.9:
            print("Obesidade grau 1")
        elif 35 <= imc < 39.9:
            print("Obesidade grau 2")   
        else:
            print("Obesidade grau 3")
    
    


    op = int(input("Digite qual opção você quer:"))