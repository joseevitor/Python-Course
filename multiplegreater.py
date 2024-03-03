

salary = float(input('What is the clerk salary? '))

if salary <= 1250:
    new = salary + (salary * 15/100)
else:
    new = salary + (salary * 10/100)
    
print('Who received R${:.2f} now will gain/earn R${:.2f}'.format(salary, new))