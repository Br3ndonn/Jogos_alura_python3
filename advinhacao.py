from random import randint


def jogar():

    imprime_mensagem_abertura()
    print('Estou pensando em um numero de 1 a 100. Advinhe.')
    num_acertos = 0
    while True:
        escolhe_nivel()
        num_secreto = randint(1, 100)
        num_palpite = 1
        acerto = False
        while num_palpite <= nivel:  #nivel se refere a quantidade de chances
            palpite = int(input('Advinhe o numero: '))
            num_palpite += 1
            if nivel == 10:
                if num_palpite == 5:
                    dica(nivel, num_secreto)
            if palpite == num_secreto:
                desenha_linha()
                print(f'PARABENS. VOCE ACERTOU O NUMERO {num_secreto} COM {num_palpite - 1} PALPITES ')
                desenha_linha()
                acerto = True
                num_acertos += 1
                jogar_novamente(num_acertos)
                break
            else:
                if num_palpite <= nivel:
                    if palpite < num_secreto:
                        print('Seu palpite foi baixo.')
                    elif palpite > num_palpite:
                        print('Seu palpite foi alto.')
            if num_palpite == nivel:
                print('Ultima chance')
        if acerto is not True:
            desenha_linha()
            print(f'VOCE PERDEU. O NUMERO SECRETO ERA {num_secreto}')
            desenha_linha()
            jogar_novamente(num_acertos)


def imprime_mensagem_abertura():
    print("*********************************")
    print("*Bem vindo ao jogo de Advinhação!*")
    print("*********************************")


def escolhe_nivel():
    global nivel
    nivel = 0
    print("[1] FÁCIL - 10 chances"
          "\n[2] NORMAL - 5 chances"
          "\n[3] DIFÍCIL - 3 chances")
    while nivel != 1 and nivel != 2 and nivel != 3:
        nivel = int(input("Defina o nivel de dificuldade: "))
    if nivel == 1:
        nivel = 10
        desenha_linha()
        print('NIVEL FACIL')
        desenha_linha()
    elif nivel == 3:
        nivel = 3
        desenha_linha()
        print('NIVEL DIFICIL')
        desenha_linha()
    else:
        nivel = 5
        desenha_linha()
        print('NIVEL MÉDIO')
        desenha_linha()

    return nivel


def jogar_novamente(num_acertos):
    while True:
        resp = input('Deseja jogar novamente? [S/N]').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Somente S ou N')
    if resp == 'S':
        jogar()
    else:
        desenha_linha()
        print(f'VOCE ACERTOU {num_acertos} VEZES')
        desenha_linha()
        quit()


def dica(nivel, num_secreto):
    if num_secreto > 1:
        for n in range(2, num_secreto + 1):
            if (num_secreto % n) == 0:
                print('Numoro não é primo')
                break
            else:
                print(f'DICA: O numero secreto é PRIMO')
                break


def desenha_linha():
    print('=='*25)


if(__name__ == "__main__"):
    jogar()
