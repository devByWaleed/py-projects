'''
Level one operators:-

As we discussed before there is an order in math.

The operators '*', '/' and '%' calculated before '+' and '-'.

In this course we call to the operators '*', '/' and '%' - level one operators.

And the operators '+' and '-' - level two operators.


Challenge:-

Currently struct only supports level two operators.

Your task is to add support for level one operators for struct.

Make sure the order of calculations is taking place!

Examples:

struct([3, '*', 2])  ->  ['*', 3, 2]
struct([1, '+', 2, 'mul', 3])  ->  ['+', 1, ['mul', 2, 3]]
struct([2, 'mod', 3, '-', 4, '/', 5.2])  ->  ['-', ['mod', 2, 3], ['/', 4, 5.2]]

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
        if op == '-':
            return -num1  # or handle unary operations here
        else:
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
    if isinstance(expression, (str, int)) or len(expression) == 0 or len(expression) > 3:
    # if isinstance(expression, str) or isinstance(expression, int) or len(expression) == 0 or len(expression) > 3:
        return(f'Failed to evaluate "{expression}"')

    operator = expression[0]

    # If the expression has only one operand (unary operation)
    if len(expression) == 2:
        num1 = expression[1]

        # If num1 is a list, evaluate it first
        if isinstance(num1, list):
            num1 = eval(num1)

        return calc(operator, num1)

    # If the expression has two operands (binary operation)
    elif len(expression) == 3:
        num1 = expression[1]
        num2 = expression[2]

        # Recursively evaluate num1 if it is a list
        if isinstance(num1, list):
            num1 = eval(num1)

        # Recursively evaluate num2 if it is a list
        if isinstance(num2, list):
            num2 = eval(num2)

        return calc(operator, num1, num2)

def struct(given_structure):

    # Logic For Level 1 Operator:

    i = 0   # From 1st Array Element

    while i < len(given_structure):

        # Checking For Level 1 Operator
        if given_structure[i] in ['*', '/', '%', 'mod', 'div', 'mul']:

            # Making Nested Structure (Where The Index Will Lie)
            given_structure[i-1:i+2] = [[given_structure[i], given_structure[i-1], given_structure[i+1]]]
            i -= 1  # Recheck the current position after replacement
        else:
            i += 1      # For Looping

    # Logic For Level 2 Operator:

    i = 0 # From 1st Arary Element

    while i < len(given_structure):

        # Checking For Level 1 Operator
        if given_structure[i] in ['+', '-', 'add', 'sub']:

            # Making Nested Structure (Where The Index Will Lie)
            given_structure[i-1:i+2] = [[given_structure[i], given_structure[i-1], given_structure[i+1]]]
            i -= 1  # Recheck the current position after replacement
        else:
            i += 1      # For Looping

    return given_structure[0]       # As Our Answer Will Be Single Answer

    # # Assigning 1st number (num1)
    # result = given_structure[0]

    # # Loop Variable To Be Start Right After 1st number
    # i = 1

    # # Loop Condition So That Index Will Be In range
    # while i < len(given_structure):

    #     # Assigning operator
    #     op = given_structure[i]

    #     # Assigning The Number Next To The Operator 
    #     number = given_structure[i+1]

    #     # Updating 1st Number To The Structure
    #     result = [op, result, number]

    #     # Incrementing By 1 Creates IndexError
    #     # So We Increase It By 2 So That It Prevents Un-necessaary Iterations
    #     i += 2

    # return result


print(struct(([3, '*', 2])))                          # ['*', 3, 2]
print(struct(([1, '+', 2, '*', 3])))                  # ['+', 1, ['*', 2, 3]]
print(struct(([2, '%', 3, '-', 4, '/', 5.2])) )       # ['-', ['%', 2, 3], ['/', 4, 5.2]]
print(struct(([1, 'add', 2, 'mod', 3, '-', 4])))      # ['-', ['add', 1, ['mod', 2, 3]], 4]
print(struct([5, '-', 5, 'mul', 5, 'div', 5]))        # ['-', 5, ['div', ['mul', 5, 5], 5]]