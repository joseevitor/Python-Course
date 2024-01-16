#def calculate_factorial(number):
 #   print("the result is" + number) 

  #  while number >= 1:
   # number = (number * (number-1))
    #if number == 1:
     #   break
    #print(c)

# number = int(input("Which value represents number? "))
# number = int(input("Which value represents the number? "))

def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result
        
#print(calculate_factorial(number))        