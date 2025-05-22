'''
Multiple Options Question:-


Challenge:-
Create a class MultiOptionsQuestion which inherits from Question and implements constructor and the methods print and check from Question class.


Constructor - should get string, list of strings and integer, and save them under the fields question, options  and answer_index accordingly.


print method - prints the question in the format,
[?] {question}
[1] {options[0]}
[2] {options[1]}
.
.
.
For example, if the question is 'How many states are in the USA?' and the options are ['49', '50', '51', '32'],
[?] How many states are in the USA?
[1] 49
[2] 50
[3] 51
[4] 32
 

check method - returns True if input string (the answer) is equal to answer_index + 1, otherwise False

Note, the input of check method is string you must cast it to integer!
'''



from abc import ABC, abstractmethod

class Question(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def check(self, user_input):
        pass


class YesNoQuestion(Question):

    # Constructor with question and answer
    def __init__(self, string, condition):
        self.question = string
        self.answer = condition

    # Printing The Question In Required Format
    def print(self):
        print(f'[?] {self.question} (yes/no)')

    # To Check The Given Conditions
    def check(self, user_input):

        if user_input == 'yes' and self.answer == True:
            return True
        elif user_input == 'no' and self.answer == False:
            return True
        else:
            return False
    
        
class OpenQuestion(Question):

    # Constructor with question and answer
    def __init__(self, string, ans_list):
        self.question = string
        self.answers = ans_list

    def print(self):
        print(f'[?] {self.question}')

    # To Check The Given Conditions
    def check(self, user_input):

        if user_input in self.answers:
            return True
        else:
            return False


class MultiOptionsQuestion(Question):
    
    # Constructor with question and answer
    def __init__(self, string, str_list, index):
        self.question = string
        self.options = str_list
        self.answer_index = index

    def print(self):
        print(f'[?] {self.question}\n')
        for i in range(len(self.options)):
            print(f'[{i+1}] {self.options[i]}')

    # To Check The Given Conditions
    def check(self, user_input):

        user_input = int(user_input)

        return user_input == self.answer_index + 1
        # if user_input == self.answer_index + 1:
        #     return True
        # else:
        #     return False



# Test Cases
obj1 = MultiOptionsQuestion("How many states are in the USA?", ['49', '50', '51', '32'], 1)
print(f"{obj1.question}\n{obj1.options}\n{obj1.answer_index}")
'''
How many states are in the USA?
49,50,51,32
1
'''

obj2 = MultiOptionsQuestion("How many states are in the USA?", ['49', '50', '51', '32'], 1)
obj2.print()
print(obj2.check(2))
print(obj2.check(4))
'''
[?] How many states are in the USA?

[1] 49
[2] 50
[3] 51
[4] 32
True
False
'''

obj3 = MultiOptionsQuestion("Do you like coding?", ["sometimes", "no", "maybe", "always!"], 3)
print(obj3.check(1))
print(obj3.check(2))
print(obj3.check(3))
print(obj3.check(4))
'''
False
False
False
True
'''