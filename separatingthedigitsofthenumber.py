number = int(input('Tell which number you wnat: '))


n = str(number)

print('Analysing the number {}'.format(number))
print('Unity: {}'.format(n[3]))
print('Ten: {}'.format(n[2]))
print('Hundred: {}'.format(n[1]))
print('Thousend: {}'.format(n[0]))

#another way to do the same thing

u = number // 1 % 10 
t = number // 10 % 100
h = number // 100 % 1000
t = number // 1000 % 10000

print('Analysing the number {}'.format(number))
print('Unity: {}'.format(u))
print('Ten: {}'.format(t))
print('Hundred: {}'.format(h))
print('Thousend: {}'.format(t))