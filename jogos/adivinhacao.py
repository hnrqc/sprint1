import random
print("********************************")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("********************************")

numero_secreto = random.randrange(1,101)
print(numero_secreto)
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite Seu Número Entre 1 e 100: ")
    chute = int(chute)
    if (chute<1 or chute>100):
        print("Voce Deve Digitar Um Numero Entre 1 e 100")
        continue
    print("Você Digitou", chute)


    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if (acertou):
        print("Você Acertou!!")
        break
    else:
        if(maior):
            print("O seu chute foi pra cima")
        elif (menor):
            print("O seu chute foi pra baixo")

    rodada = rodada + 1



print("Fim Do Jogo.")
