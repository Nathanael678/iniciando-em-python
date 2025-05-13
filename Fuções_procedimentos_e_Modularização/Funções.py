def soma(n1, n2):#101
    print(f"A soma de {n1} e {n2} é: {n1 + n2}")
    return n1 + n2

def fatorial(n):#102
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
def primo(n):#103
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def notas(n1, n2, n3):#104
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def Celsius_para_Fahrenheit(celsius):#105
    return (celsius * 9/5) + 32

def impar_ou_par(n):#106
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
def numero_de_letras(n):#107
    quantidade = len(str(n))
    return quantidade

def maior_de_tres(n1, n2, n3):#108
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    
def area_circulo(raio):#109
    pi = 3.14
    return pi * (raio ** 2)

def bem_vindo(name):#110
    return f"Bem-vindo: {name}"

def valor_absoluto(n):#111
    if n < 0:
        return -n
    else:
        return n
    
def potencia(base, expoente):##112
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado

def tabuada(n):#113
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
def menor_da_lista(lista):#114
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def indice_da_lista(lista):#115
    lista = [1, 2, 3, 4, 5]
    for i in range(len(lista)):
        print(f"Índice {i} tem o valor {lista[i]}")

def inverte_string(s):#116
    return s[::-1]

def mutiplo_de_outro(n1,n2):#117
    if n1 % n2 == 0:
        return True
    else:
        return False
    
def caixa_com_nome(largura, altura, nome):#118 ESSE AQUI DEU TRABALHO
    if largura < len(nome) + 2 or altura < 3:
        print("A largura deve ser maior que o comprimento do nome + 2, e a altura pelo menos 3.")
        return

    print("╔" + "═" * (largura - 2) + "╗")  # topo

    linhas_acima = (altura - 3) // 2
    linhas_abaixo = altura - 3 - linhas_acima

    for _ in range(linhas_acima):
        print("║" + " " * (largura - 2) + "║")

    espacos = (largura - 2 - len(nome)) // 2
    linha_nome = "║" + " " * espacos + nome + " " * (largura - 2 - espacos - len(nome)) + "║"
    print(linha_nome)

    for _ in range(linhas_abaixo):
        print("║" + " " * (largura - 2) + "║")

    print("╚" + "═" * (largura - 2) + "╝")  # base

def calculadora():#119
    print("Escolha uma opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    e = int(input("Digite a opção:"))
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))

    if e == 1:
        print(f"A soma de {n1} e {n2} é: {soma(n1, n2)}")
    elif e == 2:
        print(f"A subtração de {n1} e {n2} é: {n1 - n2}")
    elif e == 3:
        print(f"A multiplicação de {n1} e {n2} é: {n1 * n2}")
    elif e == 4:
        if n2 != 0:
            print(f"A divisão de {n1} e {n2} é: {n1 / n2}")
        else:
            print("Divisão por zero não é permitida.")
    else:
        print("Opção inválida.")
    return e, n1, n2

def senha():#120
    senha_correta = "1234"
    tentativas = 3

    while tentativas > 0:
        senha_digitada = input("Digite a senha: ")
        if senha_digitada == senha_correta:
            print("Acesso permitido.")
            return True
        else:
            tentativas -= 1
            print(f"Senha incorreta. Você ainda tem {tentativas} tentativas.")

    print("Acesso negado.")
    return False

def vogal_consoante(letra):#121
    if letra.lower() in 'aeiou':
        return "Vogal"
    elif letra.lower() in 'bcdfghjklmnpqrstvwxyz':
        return "Consoante"
    else:
        return "Não é uma letra válida"
    
def quatidade_de_vogais(s):#122
    vogais = "aeiouAEIOU"
    quantidade = 0
    for letra in s:
        if letra in vogais:
            quantidade += 1
    return quantidade

def numeros_pares_vetor(vetor):#123
    pares = []
    for numero in vetor:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def media_matriz(matriz):#124
    soma = 0
    total_elementos = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
            total_elementos += 1
    return soma / total_elementos if total_elementos > 0 else 0

def validar_cpf(cpf):#125
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
def vetor_bubble_sort(vetor):#126
    n = len(vetor)
    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor

def caucular_mdc(a, b):#127
    while b:
        a, b = b, a % b
    return a

def caulcular_mmc(a, b):#128
    return abs(a * b) // caucular_mdc(a, b)

def numero_de_palavras(s):#129
    palavras = s.split()
    return len(palavras)

def senha_aleatoria(tamanho=8):#130
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def menu_modularizado():#131
    print("Escolha uma opção:")
    return 0

def converte_horas_em_minutos_segundos(horas):#132
    minutos = horas * 60
    segundos = minutos * 60
    total_segundos = (minutos * 60) + segundos
    return total_segundos

def remover_espacos(s):#133
    return s.replace(" ", "")

def soma_digitos(numero):#134
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

def desenha_uma_arvore(altura):#135
    for i in range(altura):
        print(" " * (altura - i - 1) + "*" * (2 * i + 1))
    print(" " * (altura - 1) + "|")

def letras_repetidas(s):#136
    letras = {}
    for letra in s:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
    return letras

def embaralhar_string(s):#137
    import random
    s = list(s)
    random.shuffle(s)
    return ''.join(s)

def substituir_vogais_por_asterisco(s):#138
    vogais = "aeiouAEIOU"
    for vogal in vogais:
        s = s.replace(vogal, "*")
    return s

def iniciais_do_nome(nome):#139
    iniciais = ""
    for palavra in nome.split():
        iniciais += palavra[0].upper() + "."
    return iniciais[:-1]  # Remove o último ponto

def data_valida(data):#140
    try:
        dia, mes, ano = map(int, data.split("/"))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:
            return True
        else:
            return False
    except ValueError:
        return False