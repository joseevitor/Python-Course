number = float(input('which is the first number?'))
number2 = float(input('Which is the second number?'))
number3 = float(input('Which is the third number?'))

n = [number, number2, number3]

print('The biggest number is {}'.format(max(n)))
print('The lower number is {}'.format(min(n)))

# another wat to do this question

a = float(input('which is the first number?'))
b = float(input('Which is the second number?'))
c = float(input('Which is the third number?'))

minor = a
if b<a and b<c:
    minor = b
if c<a and c<b:
    minor = c
    
#certifying who is the biggest
biggest = a
if b>a and b>c:
    biggest = b
if c>a and c>b:
    biggest = c
    
print('The lower number typed is {}'.format(minor))
print('The biggest number typed is {}'.format(biggest))