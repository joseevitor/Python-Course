# At this code we have a game that could divine the number that we thought

import random

computer = random.randint(0, 5)

# Does the computer to think
# print('Thought on the number: {}'.format(computer))

print('I will think in a number between 0 and 5. Try to guess')


# The player try to guess
player = int(input('Which number i thought? '))

if player == computer:
    print('Contratlations! You won!!')
    
else:
    print('I win!! I thought in the number {} and not inte the {}'.format(computer, player))    