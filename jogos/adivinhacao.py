print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")

numero_secreto = 42

chute = input("Digite Seu Numero: ")
chute = int(chute)
print("Você Digitou", chute)

acertou = numero_secreto == chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto
if (acertou):
    print("Você Acertou!!")
else:
    if(maior):
        print("O seu chute foi pra cima")
    elif (menor):
        print("O seu chute foi pra baixo")


print("Fim Do Jogo")
