number = int(input('Put some number: '))

print('''Chose one of the bases to convertion:
      [1]convert to bi 
      [2]convert to octail 
      [3]convert to hexadebimal''')

option = int(input('Your option: '))

if option == 1:
    print('{} converted to binary is equal as {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('{} converted to octail is equal as {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('{} converted to hexadecimal is equal to {}'.format(number, hex(number)[2:]))
else:
    print('ERROR, try again please!!')