import forca
import advin

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("[1] FORCA"
          "\n[2] ADVINHAÇÃO"
          "\n[3] SAIR")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        #print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        #print("Jogando adivinhação")
        advin.jogar()
    elif(jogo == 3):
        #SAI DO JOGO
        quit()

if(__name__ == "__main__"):
    escolhe_jogo()
