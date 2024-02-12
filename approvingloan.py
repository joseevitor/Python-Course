house = float(input('House values: '))
salary = float(input('Salary of the buyer: R$'))
years = int(input('How many years of finacying? '))
interpretattio = house / (years * 12)

minim = salary *30 / 100

print('To pay a house of R${:.2f} in {} years'.format(house, years), end='')

print('The interpretattio will be of R${:.2f}'.format(interpretattio))




#print('Comparing need to pay {} and the minym is of {}'.format(interpretattio, minim))



if interpretattio <= minim:
    print('Loan could be concced!')
else:
    print('Loan denied!')