from random import randint


items = ('Pedra', 'Papel', 'Tesoura')

computer = randint(0, 2)

print("O computador escolheu {}".format(items[computer]))

gamer = int(input("Which gonna be your play?"))
print("=="*15)
print("Computer played {}".format(items[computer]))
print("Gamer played {}".format(items[computer]))
print("=="*15)

if computer == 0:
    if gamer == 0:

    elif gamer == 1:


    elif gamer == 2:


elif computer == 1:
    if gamer == 0:


    elif gamer == 1:



    elif gamer == 2:





elif computer == 2:  
    if gamer == 0:

    elif gamer == 1:


    elif gamer == 2:  