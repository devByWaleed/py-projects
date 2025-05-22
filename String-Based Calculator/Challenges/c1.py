'''
Create function calc which gets operator and two numbers and returns the calculation result.

Examples:

calc('+', 1, 3)  ->  4

calc('*', 2, 3)  ->  6

calc('/', 1, 4) - >  0.25

calc('-', 1, 3)  ->  -2
'''


def calc(op, num1, num2):
    
    # convert the data to a string
    expression = str(num1) + op + str(num2)
    
    # evaluating with eval() function
    answer = eval(expression)

    # returning answer
    return answer
    

print(calc("+", 1, 2))    # 3