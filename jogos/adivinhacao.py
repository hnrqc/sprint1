print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")

numero_secreto = 42

chute = input("Digite Seu Numero: ")
chute = int(chute)
print("Você Digitou", chute)

if (numero_secreto == chute):
    print("Você Acertou!!")
else:
    print("Você errou")
