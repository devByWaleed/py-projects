'''
Loop Calculator:-

In this calculator, we first decide the arithmetic operation.
Then we input the desired value on how many numbers we want to perform operation.
After that, we inputs the numbers, finally we get the result.

This calculator also has functionality of continue after 1st try and exiting the loop.
For division operation, this calculator has a while loop so that user can enter the desired number for smooth running
'''

result = 0.0    # variable store the calculation result

print("************ Welcome To Loop calculator ************")

while True:
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n")
    choice = input("Enter your choice: ")

    if choice == '1':

        # Input how many numbers you want to perform operation
        total_numbers = int(input("How many Numbers You want to add? "))

        # for loop to perform the operation
        for i in range(1, total_numbers+1):
            numbers = float(input(f"Enter number {i}: "))
            result += numbers
        print(f"Result of addition: {result}")

    elif choice == '2':

        # Input how many numbers you want to perform operation
        total_numbers = int(input("How many Numbers You want to Subtract? "))

        # For Subtraction, we need to specify the 1st number to result and then perform calculation
        num1 = input("Enter number 1: ")
        result = float(num1)

        # for loop to perform the operation
        for i in range(1, total_numbers+1):
            numbers = float(input(f"Enter number {i}: "))
            result -= numbers
        print(f"Result of subtraction: {result}")

    elif choice == '3':
        result = 1

        # Input how many numbers you want to perform operation
        total_numbers = int(input("Enter How many Numbers You want to Multiply? "))

        # for loop to perform the operation
        for i in range(1, total_numbers+1):
            numbers = float(input(f"Enter number {i}: "))
            result *= numbers
        print(f"Result of multiplication: {result}")

    elif choice == '4':

        # Input how many numbers you want to perform operation
        total_numbers = int(input("Enter how many numbers You want to divide? "))

        # For Division, we need to specify the 1st number to result and then perform calculation
        num1 = (input("Enter number 1: "))
        result = float(num1)

        # for loop to perform the operation
        for i in range(2, total_numbers+1):
            numbers = float(input(f"Enter number {i}: "))

            # case for handling 0
            if numbers == 0:

                # this loop run the times user enter 0, for smooth handling of division operation without exiting loop
                while numbers == 0:
                    print("Error! division By zero Is not possible!! Input the number again.")
                    numbers = float(input(f"Enter number {i}: "))

            result /= numbers
        print(f"Result of division: {result}")


    # condition for exiting
    elif choice == '5':
        print("************ Exiting The Loop Calculator ************")
        break

    else:
        print("Please Enter a Valid Option!!")
        continue

    # case for continuing after 1st loop calculation
    if choice != '5':
        continue_option = input("Do you want to continue (y/n)? ")
        if continue_option == 'n':
            print("************ Exiting The Loop Calculator ************")
            break
