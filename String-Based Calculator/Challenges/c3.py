'''
Aliases:-

The calculator should accept alias names for each operation,

add for +
sub for -
div for /
mul for *
pow for ^
mod for %

Challenge:-
Make calc to support the alias names described above, check the test cases for any clarification.
'''

def calc(op, num1, num2):

    # The aliases containing words with corresponding operator
    aliases = {
        "add" : "+",
        "sub" : "-",
        "mul" : "*",
        "div" : "/",
        "pow" : "^",
        "mod" : "%",
    }

    # check for aliases and assigned corresponding operator
    if op in aliases.keys():
        op = aliases[op]

    # condition assigned ^ to correspond ** operator in python
    if op == "^":
        op = "**"

    # convert the data to a string
    expression = str(num1) + op + str(num2)
    
    # evaluating with eval() function
    answer = eval(expression)

    # returning answer
    return answer

print(calc("sub", 3, 5.5))      # -2.5
print(calc("mul", 1, 54.5))     # 54.5
print(calc("div", 3, 2))        # 1.5
print(calc("pow", 3, 2))        # 1.5
print(calc("add", 5, 4))        # 1.5