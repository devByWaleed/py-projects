'''
Single number operator

As we discussed in previous lesson we can add support to single number operator and not a pair.

This is some examples with eval,

eval(['-', 4])  ->  -4
eval(['+', 4, ['-', 4]])  ->  0
eval(['*', ['+', 4], ['-', 4]])  ->  -16

Challenge:-

Add support for single number operator for the eval function.
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
    # if not isinstance(expression, list) or len(expression) == 0:
    #     raise Exception("Invalid expression format")

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



print(eval(['-', 4]))                                  # -4
print(eval(['+', 4, ['-', 4]]))                        # 0
print(eval(['*', ['+', 4], ['-', 4]]))                 # -16
print(eval(['/', ['-', 4], ['*', 2, ['-', 4]]]))       # 0.5
print(eval(['-', ['*', 2, 3]]))                        # -6