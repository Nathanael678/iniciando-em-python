print("STRINGS E MANIPULAÇÃO DE TEXTOS")

op = int(input("Escolha uma opção:"))

while op != 0:
    print(15 * "-+")
    print("0 = Sair")

    if op == 171:
        print("Você escolheu a opção 171")

        n = str(input("Digite uma frase: "))
        reverso = n[::-1]
        print(reverso)

    elif op == 172:
        print("Você escolheu a opção 172")
        numero_de_vogais = 0
        vogais = "aeiou"
        n = str(input("Digite uma frase: "))
        for i in range(len(n)):
            if n in "aeiou":
                numero_de_vogais += 1
        print("Número de vogais:", numero_de_vogais)

    elif op == 173:
        print("Você escolheu a opção 173")

        n = str(input("Digite uma frase: "))
        n = n.upper()
        print(n)

    elif op == 174:
        print("Você escolheu a opção 174")

        n = str(input("Digite uma frase: "))
        if 'a' in n:
            n = n.replace('a', '@')
        print(n)

    elif op == 175:
        print("Você escolheu a opção 175")

        n = str(input("Digite uma frase: "))
        n = n.replace(" ", "")
        n = n.lower()
        if n == n[::-1]:
            print("A frase é um palíndromo")
        else:
            print("A frase não é um palíndromo")

    elif op == 176:
        print("Você escolheu a opção 176")

        n1 = str(input("Digite a primeira frase: "))
        n2 = str(input("Digite a segunda frase: "))
        if n1 == n2:
            print("As frases são iguais")
        else:
            print("As frases são diferentes")


    elif op == 177:
        print("Você escolheu a opção 177")

        n = str(input("Digite uma frase: "))
        n = n.split()
        print("Número de palavras:", n)
        
    elif op == 178:
        print("você escolheu a opção 178")

        n = str(input("Digite uma frase: "))
        n = n.split()
        n = " ".join(n)
        print("Frase sem espaços extras:", n)

    elif op == 179:
        print("Você escolheu a opção 179")

        n = str(input("Digite uma frase: "))
        n = n.split()
        maior = ""
        for i in n:
            if len(i) > len(maior):
                maior = i
        print("A palavra mais longa é:", maior)
        
    elif op == 180:
        print("Você escolheu a opção 180")

        n = str(input("Digite uma frase: "))
        n = n.split()
        print("Número de palavras:", len(n))

    elif op == 181:
        print("Você escolheu a opção 181")

        n = str(input("Digite seu nome completo: "))
        n = n.split()
        primeiro_nome = n[0]
        print("Seu primeiro nome é:", primeiro_nome)

    elif op == 182:
        print("Você escolheu a opção 182")

        n = str(input("Digite seu CPF: "))
        n = n.replace(".", "")
        n = n.replace("-", "")
        n = n.replace(" ", "")
        n = n[:3] + "." + n[3:6] + "." + n[6:9] + "-" + n[9:]
        print("Seu CPF é:", n)

    elif op == 183:
        print("Você escolheu a opção 183")

        n = str(input("Digite seu email: "))
        if "@" in n and ".com" in n:
            print("Email válido")
        else:
            print("Email inválido")

    elif op == 184:
        print("Você escolheu a opção 184")

        n = str(input("Digite uma frase: "))
        n = n.lower()
        n = n.replace(" ", "")
        letras = {}
        for i in n:
            if i in letras:
                letras[i] += 1
            else:
                letras[i] = 1
        for i in letras:
            print(i, ":", letras[i])
            
    elif op == 185:
        print("Você escolheu a opção 185")

        n = str(input("Digite seu nome: "))
        n = n.lower()
        n = n.replace(" ", "")
        nomes = []
        if n in nomes:
            print("Nome já cadastrado")
        else:
            nomes.append(n)
            print("Nome cadastrado com sucesso")
            
    elif op == 186:
        print("Você escolheu a opção 186")

        #tranforme a primeira letra de cada palavra em maiúscula
        n = str(input("Digite uma frase: "))
        n = n.split()
        for i in range(len(n)):
            n[i] = n[i].capitalize()    
        n = " ".join(n)
        print("Frase com a primeira letra de cada palavra em maiúscula:", n)
        
    elif op == 187:
        print("Você escolheu a opção 187")

        n = str(input("Digite uma frase: "))
        n = n.split()
        for i in range(len(n)):
            n[i] = n[i][::-1]
        n = " ".join(n)
        print("Frase com as palavras invertidas:", n)

    elif op == 188:
        print("Você escolheu a opção 188")

        n = str(input("Digite uma frase: "))
        n = n.replace("e", "&")
        n = n.replace("E", "&")
        print("Frase com as letras e trocadas por &:", n)

    elif op == 189:
        print("Você escolheu a opção 189")

        n = str(input("Digite uma frase: "))
        letra = str(input("Digite uma letra: "))
        n = n.lower()
        letra = letra.lower()
        cont = 0
        for i in n:
            if i == letra:
                cont += 1
        print("A letra", letra, "aparece", cont, "vezes na frase")
        
    elif op == 190:
        print("Você escolheu a opção 190")

        n = int(input("Digite um número de 0 a 10: "))

        if n == 0:
            print("Zero")
        elif n == 1:
            print("Um")
        elif n == 2:
            print("Dois")
        elif n == 3:
            print("Três")
        elif n == 4:
            print("Quatro")
        elif n == 5:
            print("Cinco")
        elif n == 6:
            print("Seis")
        elif n == 7:
            print("Sete")
        elif n == 8:
            print("Oito")
        elif n == 9:
            print("Nove")
        elif n == 10:
            print("Dez")

    else:
        print("Opção inválida!")
    print(15 * "-+")
    print("0 = Sair")
    op = int(input("Esolha uma opção de 141 a 170: "))
    if op == 0:
        print("Saindo...")
        break