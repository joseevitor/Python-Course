firstlinesegment = float(input('Tell me the value of the first line segment: '))
secondlinesegment = float(input('Tell me the value of the second line segment: '))
thirdlinesegment = float(input('Tell me the value of the third line segment: '))


if firstlinesegment == secondlinesegment == thirdlinesegment:
    print('This is an EQUILATERAL TRIANGLE!!')
elif firstlinesegment == secondlinesegment > thirdlinesegment or firstlinesegment == thirdlinesegment > secondlinesegment or secondlinesegment == thirdlinesegment > firstlinesegment:
    print('This is an ISOSCELES TRIANGLE!!!')
elif firstlinesegment == secondlinesegment + thirdlinesegment or secondlinesegment == firstlinesegment + thirdlinesegment or thirdlinesegment == firstlinesegment + secondlinesegment:
    print('This is not a TRIANGLE!!!')
