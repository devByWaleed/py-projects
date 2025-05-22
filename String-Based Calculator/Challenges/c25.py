'''
Main function:-

After having the coordinate function what left is to add the option to take input from the user and calling coordinate.

Try making it inside the "main function" in python (read more),

if __name__ == '__main__':
    ...

Challenge:-
Ask for input from the user and print the result of the calculation.
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
        elif op == "%":
            return num1 % num2
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

    special_chars = {'!', '@', '#', '$', '%', '&', '_', '=', 
                 '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>',
                  '?', '`', '~'}


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
            elif (expression[i] in special_chars):
                raise Exception(f'Invalid operator "{expression[index:i+1]}"')
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



def pre_parse(pair_exp):

    # Using Stack For Checking Parenthesis
    stack = []
    for i in pair_exp:
        if i == '(':
            stack.append(i)     # Append To Stack
        elif i == ')':
            if not stack:
                raise Exception("Not matching parenthesis")
            stack.pop()         # If Stack is not empty, Then Pop The Added One

    # If Stack Is Not Empty, Then Parenthesis is incomplete
    if stack:
        raise Exception("Not matching parenthesis")
    else:
        return parse(pair_exp)




def parse(str_expression):

    # Remove WhiteSpaces In The String
    if " " in str_expression:
        str_expression = str_expression.replace(" ", "")

    # List We Give To struct() method To Return Desired Structure
    lst_expression = []

    # Looping Over String
    i = 0
    while i < len(str_expression):

        # Code Block To Handle Expression Indide ()
        if str_expression[i] == '(':
            start = i + 1       # To Keep Track Of String Inside ()
            end = start         # To Keep Track Of Corresponding ) of () pair
            count = 1           # To Keep Track Of Nested ()
            parenthesis_exp = ''


            while end < len(str_expression):
                if str_expression[end] == '(':
                    count += 1
                elif str_expression[end] == ')':
                    count -= 1
                    if count == 0:
                        break
                parenthesis_exp += str_expression[end]
                end += 1
            
            # Recursive Call To Grab Structure Form
            pair_struct = parse(parenthesis_exp)

            # Appending To List ( We Give To struct() method )
            lst_expression.append(pair_struct)

            # Updating The Loop Counter To Continue Process after )
            i = end + 1
        
        else:
            # get_next() To Handle Numbers, Operators And Aliases
            value = get_next(str_expression, i)

            # Unpacking The Value And Index
            current_val , current_index = value
            lst_expression.append(current_val)
            i = current_index
        
    # Returning The Fully-Final Structure
    return struct(lst_expression)


def coordinate(user_input):
    try:
        parenthesis = pre_parse(user_input)
        return eval(parenthesis)
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    user_input = input()
    print(coordinate(user_input))

# print(coordinate('1.2 +  3.7'))                 # 4.9
# print(coordinate('(1+2)*(3*2) / (-  2)'))       # -9.0
# print(coordinate('1+2?3+4'))                    # Error: Invalid operator "?"
# print(coordinate('1+2mod3+4'))                  # 7
# print(coordinate('1+2mod (3 sub 1)'))           # 1
# print(coordinate('2 test 3'))                   # Error: Invalid operator "test"
# print(coordinate('2*(3 + 4))'))                 # Error: Not matching parenthesis
# print(coordinate('- (2 pow (3 sub 4))'))        # -0.5