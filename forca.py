from random import randrange


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    erros = 0
    tentativas = 0
    print(" _ " * len(palavra_secreta))

    while True:
        chute = input('Qual letra?').strip().lower()
        tentativas += 1
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros = erros + 1
            desenha_forca(erros)
            if erros >= 1:
                print(f'Vc errou. Faltam {7-erros} chances')
        if erros == 7:
            break
        if "_" not in letras_acertadas:
            break
        print(letras_acertadas)

    if "_" not in letras_acertadas:
        imprime_mensagem_vencedor()
        jogar_novamente()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        jogar_novamente()


def jogar_novamente():
    while True:
        resp = str(input('Deseja jogar novamente? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Somente S ou N.')
    if resp == 'S':
        jogar()
    else:
        quit()


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    palavras = list()
    with open("palavras.txt", "r") as arquivo:  # abri o arquivo de texto com as palavras a serem sorteadas
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_perdedor(palavra_secreta):
    print("=-" * 30)
    print("Puxa, você foi enforcado!")
    print("=-" * 30)
    print(f"A palavra era {palavra_secreta}")
    print("=-" * 30)
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("=-" * 30)
    print("Parabéns, você ganhou!")
    print("=-" * 30)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if (__name__ == "__main__"):
    jogar()

