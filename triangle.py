import math

triangle = 180
length = float(input('Whats the value of the oposite length? '))
adjlength = float(input('whats the value of the length adjacent? '))

hypotenuse = math.hypot(length, adjlength)


print('the value of hypotenuse is {}'.format(hypotenuse))