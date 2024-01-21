import random

std1 = str(input('First student: '))
std2 = str(input('Second student: '))
std3 = str(input('Third student: '))
std4 = str(input('Fourth student: '))

students = [std1, std2, std3, std4]
random.shuffle(students)

print('The order of the apresentation will be {}'.format(students))