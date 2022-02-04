import forca
import adivinhacao

print("********************************")
print("*******ESCOLHA SEU JOGO!********")
print("********************************")

print("(1) FORCA   (2) ADIVINHAÇÃO")

jogo = int(input("QUAL JOGO?: "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()
