'''
Recursive structure:-

The real power of the structure we saw last lesson comes with recursion.

Consider calculation with more than one operator, for example:

2 + 3 * 4 + 5
There is an order according to math rules, first we need to calculate 3 * 4 and then all the rest.

The following calculation will be formatted into recursive structure in the possible ways,

['+', ['+', 2, ['*', 3, 4]], 5]
['+', 2, ['+', 5, ['*', 3, 4]]]
['+', 5, ['+', ['*', 3, 4], 2]]
Notice that the deepest simple structure is always ['*', 3, 4] which is the first to calculate, also note that everything is the basic structure [op, num1, num2]. 

Some more examples of calculations to recursive structure:

2 - 3              ->           ['-', 2, 3]
1 - 2 + 3          ->           ['+', ['-', 1, 2], 3]
1 * 2 - 3          ->           ['-', ['*', 1, 2], 3]
2.3 + 3 / 4.2 - 2  ->           ['-', ['+', 2.3, ['/', 3, 4.2]], 2]

Challenge

Upgrade the eval function to support recursive structures as described above.

Notes:

call calc function when the structure is simple structure, operator with two numbers.
call eval recursively if one of the arguments is another structure (list).
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
    # if len(expression) != 3:
    #     raise Exception("Invalid expression format. Expected format: [op, num1, num2]")
    
    operator = expression[0]
    num1 = expression[1]
    num2 = expression[2]

    if isinstance(num1, list):
        answer = eval(num1)
        num1 = answer
        
        return calc(operator, answer, num2)
    elif isinstance(num2, list):
        answer = eval(num2)
        num2 = answer
        return calc(operator, num1, answer)
    else:
        return calc(operator, num1, num2)


print(eval(['+', ['-', 1, 2], 3]))                 # 2
print(eval(['-', 1, ['+', 2, 3]]))                 # -4
print(eval(['+', ['+', 2, ['*', 3, 4]], 5]))       # 19
print(eval(['/', 1, 2]))                           # 0.5
print(eval(['*', 2, ['+', 1, 2]]))                 # 6