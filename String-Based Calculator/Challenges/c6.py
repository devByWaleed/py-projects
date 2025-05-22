'''
Basic structure:-

The next step is to evaluate list of expressions.

The basic structure is - [op, num1, num2]

Some examples:

['+', 1, 2]  ->  calc('+', 1, 2)
['*', 3, 2]  ->  calc('*', 3, 2)
['/', 5.3, 0]  ->  calc('/', 5.3, 0)

Challenge

create function eval which gets basic structure, a list as described above, and returns the calculation result.

Use the calc function you created!
'''


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
    
    
def eval_structure(structure):
    operator = structure[0]
    num1 = structure[1]
    num2 = structure[2]

    answer = calc(operator, num1, num2)
    return answer


print(eval_structure(['+', 1, 2]))        # 3
print(eval_structure(['*', 6, 3.5]))      # 21.0
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

    # Check if num1 is a valid number
    if not isinstance(num1, (int, float)):
        raise Exception(f'Invalid number "{num1}"')

    # If num2 is provided, check if it's a valid number
    if num2 is not None and not isinstance(num2, (int, float)):
        raise Exception(f'Invalid number "{num2}"')

    # Check for aliases and assign corresponding operator
    op = aliases.get(op, op)

    # Condition assigned ^ to correspond ** operator in Python
    if op == "^":
        op = "**"

    # Validate operator after alias resolution
    if op not in ["+", "-", "*", "/", "**", "%"]:
        raise Exception(f'Invalid operator "{op}"')

    # If 2nd number is not given, return the number itself (or handle unary operation)
    if num2 is None:
        return num1  # or handle unary operations here

    # Try to solve the expression
    try:
        # Division by zero check before evaluating
        if op in ["/", "%"] and num2 == 0:
            raise Exception('Division by zero')

        # Perform the operation directly without eval
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2
        elif op == "**":
            return num1 ** num2

    except Exception as e:
        raise Exception(f'{str(e)}') from e


def eval(expression):
    if len(expression) != 3:
        raise Exception("Invalid expression format. Expected format: [op, num1, num2]")

    operator = expression[0]
    num1 = expression[1]
    num2 = expression[2]

    return calc(operator, num1, num2)


# Testing the eval function with some examples
print(eval(['+', 1, 2]))         # Should output: 3
print(eval(['*', 3, 2]))         # Should output: 6
try:
    print(eval(['/', 5.3, 0]))       # Should raise an exception for division by zero
except Exception as e:
    print(e)
print(eval(['-', 10, 4]))        # Should output: 6
print(eval(['pow', 2, 3]))       # Should output: 8 (if 'pow' is handled in calc)
