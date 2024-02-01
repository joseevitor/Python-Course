speed = float(input('What is your speed? '))

# print('have a good day, drive with security!!')

if speed < 81:
    print('have a good day, drive with security!!')
else:
    print('FINED!! You pass of the limith than is 80km/h')
    fine = (speed - 80) * 7
    print('You must pay a fine of R${:.2f}!'.format(fine))
