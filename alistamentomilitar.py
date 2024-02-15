from datetime import date

atual = date.today().year

born = int(input('Your birth date: '))

age = atual - born

print('Who borned in {} have {} years in {}'.format(born, age, atual))

if age == 18:
    print('You need to give your name immediatly')
elif age < 18:
    saldo = 18 - age
    print('Ainda faltam {} anos para o seu alistamento'.format(saldo))
elif age > 18:
    saldo = age - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))