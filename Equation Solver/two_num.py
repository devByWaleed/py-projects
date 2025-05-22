# Importing permutation
from itertools import permutations
import re, time, tracemalloc



start_time = time.time()

tracemalloc.start()

def equation(given):

    # Extract all numbers from the input string
    given_numbers = re.findall(r'\d+', given)
    
    if len(given_numbers) != 3:
        return None  # Not valid input format

    # Unpack The Values And Answer
    A, B, answer = given_numbers

    # Converting All To Integers From String
    A, B, answer = int(A), int(B), int(answer)

    op = {'+', '-', '*', '/', '**'}

    # pair = {A: "A", B: "B"}

    for i in op:

        # Making permutations
        all_perms = permutations([A, B, i])

        # Converting itertools object to list
        all_perms = list(all_perms)

        # This list will save all valid permutations (start & end with number)
        valid_perms = []


        # Looping over all_perms to check for correct permutation
        for i in all_perms:

            # adding all valid permutations (start & end with number) to valid_perms
            if str(i[0]).isdigit() and str(i[-1]).isdigit():
                valid_perms.append(i)


        # Looping over final_pers to check for correct permutation
        for j in valid_perms:

            # converting the list to string
            expression = " ".join(map(str, j))

            calc_answer = eval(expression)


            # checking and printing that permutation
            if calc_answer == answer:
                return expression, calc_answer, True



# List of input strings
# eq1 = input("Enter 1st Equation: ")
# eq2 = input("Enter 2nd Equation: ")
# eq3 = input("Enter 3rd Equation: ")
# equations = [eq1, eq2, eq3]
equations = ["20, 5 = 4", "25, 5 = 5", "30, 3 = 10"]

# Loop through each input and print the result
for eq in equations:
    result = equation(eq)
    ans_format, answer, status = result
    print(f"{eq.center(12, ' ')} | {ans_format} = {str(answer).center(6, ' ')} -> {status}")

end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time = elapsed_time * 1000
print(f"Execution Time: {elapsed_time:.2f} ms")

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Current memory usage: {current / 10**6:.2f} MB")
print(f"Peak memory usage: {peak / 10**6:.2f} MB")


# print("-" * 183)
# print(f"All Possible Permutations:-\n{all_perms}")
# print("-" * 183)
# print(f"All valid Permutations:-\n{valid_perms}")
# print("-" * 183)
'''

'''