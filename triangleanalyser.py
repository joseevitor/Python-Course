r1 = float(input('First segment: '))
r2 = float(input('Second segment:'))
r3 = float(input('Third segment: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('The sigments on up could make a triangle')
else:
    print('The sigments ahead can not make a triangle')