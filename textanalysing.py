phrase = str(input('Write your name: ')).strip()

print('Your name with uppercase letters is {}'.format(phrase.upper()))

print('Your name with lowercase letters is {}'.format(phrase.lower()))

name = phrase.split()
print('The first name is {}, and it has {} letters'.format((name[0]),len(name[0])))

print('Your name has {} letters'.format(len(phrase)-phrase.count(' ')))
