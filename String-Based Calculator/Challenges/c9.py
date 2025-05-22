'''
Handling errors:-

Currently eval not considering invalid input, the possible errors:

Not list as input.
Wrong size of list, only acceptable sizes are 2 and 3.

Challenge:-

Add exception handling for the above errors.

Some examples of the error messages by calls:

eval('not a list')  ->  Failed to evaluate "not a list"
eval([])  ->  Failed to evaluate "[]"
eval(['+', 2, 3, 4])  ->  Failed to evaluate "['+', 2, 3, 4]"
eval(5)  ->  Failed to evaluate "5"
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


print(eval("not a list"))           # Failed To evaluate "not a list"
print(eval([]))                     # Failed To evaluate "[]"
print(eval(['+', 2, 3, 4]))         # Failed To evaluate "['+', 2, 3, 4]"
print(eval(5))                      # Failed To evaluate "5"