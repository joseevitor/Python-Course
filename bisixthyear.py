import datetime



year = int(input('Which year want to analyze? '))

if year == 0:
    year = datetime.date.today().year

if year % 4 == 0:
    print('The year {} is bisixth'.format(year))
else:
    print('The year {} is not bisixth'.format(year))