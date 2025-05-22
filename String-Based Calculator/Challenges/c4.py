'''
Handling errors:-

There are some possible errors we should consider,

Division by zero - calc('/', 3, 0) or calc('%', 5, 0)
Invalid operator - calc('$', 3, 2)
Invalid number - calc('+', 'not_a_number', 2)

Challenge:-

Add to calc option to raise an exceptions when the above errors happen.

The error messages should be in the following formats,

calc('/', 3, 0)  ->  Division by zero
calc('$', 3, 2)  ->  Invalid operator "$"
calc('+', [], 3)  ->  Invalid number "[]"


Note:   Number is of type int or float
'''



def calc(op, num1, num2):
    # The aliases containing words with corresponding operator
    aliases = {
        "add": "+",
        "sub": "-",
        "mul": "*",
        "div": "/",
        "pow": "^",
        "mod": "%",
    }

    # Check if num1 and num2 are valid numbers
    if not isinstance(num1, (int, float)):
        raise Exception(f'Invalid number "{num1}"')
    
    if not isinstance(num2, (int, float)):
        raise Exception(f'Invalid number "{num2}"')

    # Check for aliases and assign corresponding operator
    if op in aliases.keys():
        op = aliases[op]

    # Condition assigned ^ to correspond ** operator in Python
    if op == "^":
        op = "**"

    # Validate operator after alias resolution
    if op not in ["+", "-", "*", "/", "**", "%"]:
        raise Exception(f'Invalid operator "{op}"')

    

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



try:
    print(calc('??', 5.4, 'not_a_number'))  # Expected: Invalid number "not_a_number"
except Exception as e:
    print(e)

try:
    print(calc('/', 3, 0))                   # Expected: Division by zero
except Exception as e:
    print(e)

try:
    print(calc('$', 3, 2))                   # Expected: Invalid operator "$"
except Exception as e:
    print(e)

try:
    print(calc('+', [], 3))                  # Expected: Invalid number "[]"
except Exception as e:
    print(e)
