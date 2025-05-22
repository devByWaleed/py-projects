'''
Add support for the operators -

% - modulo operator
^ - power operator, 2^3 equal to 23
'''

def calc(op, num1, num2):
    # condition assigned ^ to correspond ** operator in python
    if op == "^":
        op = "**"

    # convert the data to a string
    expression = str(num1) + op + str(num2)
    
    # evaluating with eval() function
    answer = eval(expression)

    # returning answer
    return answer

print(calc("^", 2, 3))    # 8
print(calc("%", 5, 2))    # 1