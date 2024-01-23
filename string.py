frase = 'Curso em Video Python'

print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
len(frase)
frase.count('o')
frase.count('o', 0, 13)
frase.find('deo')

# quando não há o que se encontrar o retorno é -1 
frase.find('Android')

curso in frase

# TRANFORMATION METHODS
frase.replace('Python', 'Android')

# Make all the words upper
frase.upper()

#make with than all the words to be lower now
frase.lower()

# first letter will be upper while all the others letters will be lower
frase.capitalize()

# Now, the first letter in all the words will be upper
frase.title()

# remove all the spaces without utility
frase.strip()

# remove the spaces on the right or left side without utility
frase.rstrip()
frase.lstrip()

# DIVISION
frase.split()

# Tojoin or merge the phrases
'-'.join(frase)

