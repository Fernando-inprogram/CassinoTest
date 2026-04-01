#farei um caça níquel básico de cassino.
#a ideia é fazer um caça níquel com 3 rolos e 5 símbolos diferentes.
#quero que tenha a animação dos rolos girando e parando um por um.
#quero que o jogador possa escolher quanto apostar e que o jogo mostre o resultado da aposta.


import random
import time
InitialBalance = 1000

def reels():
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐"]
    return symbols


def spin():
    reel1 = random.choice (reels())
    reel2 = random.choice (reels())
    reel3 = random.choice (reels())
    return reel1, reel2, reel3



def graphics(reel1):
    for i in range (2):
        print ("  ___")
        i = i +1
    print (f"| {reel1} |")



def MainCassino():
    balance = InitialBalance
    while True:
        print(f"Seu saldo atual é: {balance}")
        bet =  float(input("Digite o valor da sua aposta: "))
        if bet > balance:
            print("Saldo insuficiente. Tente novamente.")
            continue
        elif bet <= 0:
            print("Você decidiu não apostar. Eu continuaria... Mas até a próxima!")
            break
        else:
             balance -= bet
            
        print("Girando os rolos...")
        time.sleep(1)
        reel1, reel2, reel3 = spin()

     # linha de cima
        print("  ___   ___   ___")
        # linha dos símbolos
        print(f"| {reel1} | ",end="")
        time.sleep(1)
        print(f"| {reel2} | ",end="")               
        time.sleep(1)
        print(f"| {reel3} |")


        if reel1 == reel2 == reel3:
            print("Parabéns, você ganhou!")
            balance += bet * 0.5
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            print("Quase lá, ganho de misericórdia!")
            balance += bet * 0.06

MainCassino()







#Cassino da IA, com frames de animação.

""" 
import random
import time

InitialBalance = 1000

def reels():
    return ["🍒", "🍋", "🍊", "🍉", "⭐"]

def spin():
    return random.choice(reels()), random.choice(reels()), random.choice(reels())

def animate_spin(final_symbols):
    reel1, reel2, reel3 = final_symbols

    # número de "frames" da animação
    frames = 10  

    for i in range(frames):
        # cada rolo mostra símbolos aleatórios até parar
        s1 = random.choice(reels()) if i < frames - 7 else reel1
        s2 = random.choice(reels()) if i < frames - 4 else reel2
        s3 = random.choice(reels()) if i < frames - 1 else reel3

        # imprime os três rolos lado a lado
        print(f"| {s1} | | {s2} | | {s3} |")
        time.sleep(0.2)

    # resultado final
    print(f"\nResultado final: | {reel1} | | {reel2} | | {reel3} |\n")

def MainCassino():
    balance = InitialBalance
    while True:
        print(f"Seu saldo atual é: {balance}")
        try:
            bet = float(input("Digite o valor da sua aposta: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        if bet > balance:
            print("Saldo insuficiente. Tente novamente.")
            continue
        elif bet <= 0:
            print("Você decidiu não apostar. Até a próxima!")
            break

        balance -= bet

        print("Girando os rolos...\n")
        final_symbols = spin()
        animate_spin(final_symbols)

        reel1, reel2, reel3 = final_symbols
        if reel1 == reel2 == reel3:
            print("Parabéns, você ganhou!")
            balance += bet * 0.5
        elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
            print("Quase lá, ganho de misericórdia!")
            balance += bet * 0.06

MainCassino()
 """







