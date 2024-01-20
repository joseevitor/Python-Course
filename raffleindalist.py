import random

#alunos = ['Tiago', 'João', 'Aline', 'José']
#escolhido = random.choice(alunos)
#print(escolhido)

student1 = str(input('First student: '))
student2 = str(input('Second student: '))
student3 = str(input('Third student: '))
student4 = str(input('Fourth student: '))

list = [student1, student2, student3, student4]
chosen = random.choice(list)

print('The chosen student is {}'.format(chosen))