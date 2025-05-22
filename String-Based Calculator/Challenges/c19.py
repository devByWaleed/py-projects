'''
Simple calculation;-

We are done with the helper function!

Now let's make the real parse function, the goal of this function is to get string and parse it into our structured format which eval gets.


Challenge:-
Create a function parse which gets string and returns a structured format.

This time we are going to deal only with simple calculation, with one operator.

Examples:

parse('1+2')  ->  ['+', 1, 2]
parse('  3*  5')  ->  ['*', 3, 5]
parse('3 pow 2.5')  ->  ['pow', 3, 2.5]
Make use of get_next and struct functions.

Note that before everything you must remove all the whitespaces!
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
    

def get_next(expression, index):
    output = ""

    all_operators = ['^', 'pow', '*', '/', '%', 'mod', 'div', 'mul', '+', '-', 'add', 'sub']

    # Add Condition For Index Error Handling
    if len(expression) == 0 or index > len(expression)-1:
        return f"End of string"
 
    # Structure To Tackle Numbers and Dot 
    if  expression[index].isdigit():

        for i in range(index, len(expression)):
            if expression[i] == '.' or  expression[i].isdigit():
                output += expression[i]
            else:
                index = i
                break
        else:
            # If loop completes without breaks
            index = len(expression)
            
        # Conditions To Cast String As Per Condition
        if '.' in output:
            output  = float(output)
            return output, index
                
        else:
            output = int(output)
            return output, index


    
        
    # Structure To Tackle Operators And Aliases
    else:        
        for i in range(index, len(expression)):
            # if (expression[i] != '.' and not(expression[i].isdigit())) or (expression[i].isalpha()):
            if (expression[i] in all_operators) or (expression[i].isalpha()):
                output += expression[i]
            else:
                index = i
                break
        else:
            # If loop completes without breaks
            index = len(expression)
    
        return output, index
               
    
    


def struct(given_structure):

    all_operators = ['^', 'pow', '*', '/', '%', 'mod', 'div', 'mul', '+', '-', 'add', 'sub']

    # Conditions For Error Handling:-
    if ((not isinstance(given_structure, list)) or (len(given_structure) == 1) or (given_structure[-1] in all_operators and len(given_structure)%2 == 0)):
        return f'Failed to structure "{given_structure}"'

    if len(given_structure) == 2:
        return given_structure
    

    


    # Logic For ^ Operator:

    i = 0 # From 1st Arary Element

    while i < len(given_structure):

        # Checking For Level 1 Operator
        if given_structure[i] in all_operators[0:2]:

            # Making Nested Structure (Where The Index Will Lie)
            given_structure[i-1:i+2] = [[given_structure[i], given_structure[i-1], given_structure[i+1]]]
            i -= 1  # Recheck the current position after replacement
        else:
            i += 1      # For Looping


    # Logic For Level 1 Operator:

    i = 0   # From 1st Array Element

    while i < len(given_structure):

        # Checking For Level 1 Operator
        if given_structure[i] in all_operators[2:8]:

            # Making Nested Structure (Where The Index Will Lie)
            given_structure[i-1:i+2] = [[given_structure[i], given_structure[i-1], given_structure[i+1]]]
            i -= 1  # Recheck the current position after replacement
        else:
            i += 1      # For Looping

    # Logic For Level 2 Operator:

    i = 0 # From 1st Arary Element

    while i < len(given_structure):

        # Checking For Level 1 Operator
        if given_structure[i] in all_operators[8:]:

            # Making Nested Structure (Where The Index Will Lie)
            given_structure[i-1:i+2] = [[given_structure[i], given_structure[i-1], given_structure[i+1]]]
            i -= 1  # Recheck the current position after replacement
        else:
            i += 1      # For Looping


    # Handling "typos" or unsupported operators
    i = 0
    while i < len(given_structure):
        # If the element is not an operator and not a number (int or float)
        if isinstance(given_structure[i], str) and len(given_structure[i]) == 1 and given_structure[i] not in all_operators:

            given_structure[i-1:i+2] = [[given_structure[i], given_structure[i-1], given_structure[i+1]]]
            i -= 1  # Recheck the current position after replacement
        else:
            i += 1
    
    
    # Handling "typos" or unsupported operators
    i = 0
    while i < len(given_structure):
        # If the element is not an operator and not a number (int or float)
        if isinstance(given_structure[i], str) and len(given_structure[i]) > 1 and given_structure[i] not in all_operators:

            given_structure[i-1:i+2] = [[given_structure[i], given_structure[i-1], given_structure[i+1]]]
            i -= 1  # Recheck the current position after replacement
        else:
            i += 1



    return given_structure[0]       # As Our Answer Will Be Single Answer


def parse(str_expression):
    if " " in str_expression:
        str_expression = str_expression.replace(" ", "")

    lst_expression = []
    # for i in range(len(str_expression)):
    i = 0
    while i < len(str_expression):
        value = get_next(str_expression, i)

        current_val , current_index = value
        lst_expression.append(current_val)
        i = current_index
        

    return struct(lst_expression)


# Calculate the start index from your previous get_next calls results.


print(parse('1+2'))             # ['+', 1, 2]
print(parse('  3*  5'))         # ['*', 3, 5]
print(parse('3 pow 2.5'))       # ['pow', 3, 2.5]