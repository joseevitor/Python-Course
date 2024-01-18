length = float(input('whats the value of the length? '))
height = float(input('Whats the value of the height? '))
area = length * height
paint = area / 2

print('The lengths value is {:.2f}mts and the heights value is {:.2f} meters. Based on these informations, we can supposed that the area corresponds at {} square meters'.format(length, height, area))
print('To paint this wall, we need to use {:.2f} liters of paint'.format(paint))