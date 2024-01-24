phrase = str(input('Write your name: ')).strip()

print('Your name with uppercase letters is {}'.format(phrase.upper()))

print('Your name with lowercase letters is {}'.format(phrase.lower()))

first_name = phrase.split()[0]
print('The first name is {}'.format(len(first_name)))

print('Your name has {} letters'.format(len(phrase)-phrase.count(' ')))
