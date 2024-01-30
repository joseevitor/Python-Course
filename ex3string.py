phrase = str(input('Tell me your phrase: ')).upper().strip()

print('The letter A appears {} times on the phrase'.format(phrase.count('A')))
print('The first letter A appears on position {}'.format(phrase.find('A')+1))
print('The last  letter A appears on position {}'.format(phrase.rfind('A')+1))