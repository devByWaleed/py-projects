'''
Single number:-

Currently the calc function supports only two numbers operations.

Let's add single number operations for '+' and '-',

calc('+', 5.4)  ->  5.4
calc('-', 3)    ->  -3

Challenge

Add support for single number operators for '+' and '-'.

Add default value, None, to the 3rd argument of calc
'''


def calc(op, num1, num2=None):
    # The aliases containing words with corresponding operator
    aliases = {
        "add": "+",
        "sub": "-",
        "mul": "*",
        "div": "/",
        "pow": "^",
        "mod": "%",
    }

    # If num2 is None, then no need to check num2 type
    if num2 is None:
        pass
    else:
        # Check if num2 are valid numbers
        
        if not isinstance(num2, (int, float)):
            raise Exception(f'Invalid number "{num2}"')

    # Check if num1 are valid numbers
    if not isinstance(num1, (int, float)):
        raise Exception(f'Invalid number "{num1}"')

    # Check for aliases and assign corresponding operator
    if op in aliases.keys():
        op = aliases[op]

    # Condition assigned ^ to correspond ** operator in Python
    if op == "^":
        op = "**"


    # Validate operator after alias resolution
    if op not in ["+", "-", "*", "/", "**", "%"]:
        raise Exception(f'Invalid operator "{op}"')

    
    # If 2nd number is not given, perform operation on single number
    if num2 == None:
        expression = op + str(num1)
        answer = eval(expression)
        return answer

    # Try to solve the expression
    try:
        # Division by zero check before evaluating
        if op in ["/", "%"] and num2 == 0:
            raise Exception('Division by zero')

        # Convert the data to a string
        expression = str(num1) + op + str(num2)

        # Evaluating with eval() function
        answer = eval(expression)

        # Returning answer
        return answer

    except Exception as e:
        raise Exception(f'{str(e)}') from e


print(calc("+", 3))
print(calc("-", 2.5))
print(calc("-", 6.8, None))


try:
    print(calc('???', 6))  # Expected: Invalid operator "???"
except Exception as e:
    print(e)

try:
    print(calc('add', [1]))   # Expected: Invalid number "[1]"
except Exception as e:
    print(e)