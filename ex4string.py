name = str(input('What is your name? ')).strip()

nameint = name.split()
print('Nice to meet you {}!'.format(name))
print('Your first name is {}'.format(nameint[0]))
print('Your last name is {}'.format(nameint[len(nameint)-1]))

