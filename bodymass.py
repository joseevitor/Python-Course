weight = float(input('What is your weight? (Kg)' ))

height = float(input('Whats is your height? (m)'))

MBI = weight / (height ** 2)


print('The mass body index of this person is {:.1f}'.format(MBI))

if MBI < 18.5:
    print('The person has desnutrition! Take care of your body')

if 18.5 <= MBI <= 25:
    print('The person has de ideal weight! Good job')

if 