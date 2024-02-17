note1 = float(input('Tell me your first testing note: '))
note2 = float(input('Tell me your second testing note: '))

middle = (note1 + note2) / 2
print('with {:.1f} and {:.1f}, the middle of the studenbt will be {:.1f}'.format(note1, note2, middle))

if middle >= 3.5 and middle <= 7:
    print('The student is in RECOVERY!!')

elif middle < 3.5:
    print('The student is FAILED!!')

else:
    print('The student is APPROVED!!')
#print('With {} the student will be in recovery yet')
#print('The student is in recovery')