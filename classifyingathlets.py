from datetime import date

year = date.today().year
print(year)
born = int(input('Tell me your born year: '))

age = year - born

print('The athlet is {} years old'.format(age))

if age <= 9:
    print('Class: Child')
elif age <= 14:
    print('Class: Kiddie')
elif age <= 19:
    print('Class: Junior')
elif age <= 25:
    print('Class: Senior')
else:
    print('Class: Master')