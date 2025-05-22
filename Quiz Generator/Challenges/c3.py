'''
Open Question:-


Challenge:-
Create a class OpenQuestion which inherits from Question and implements constructor and the methods print and check from Question class.


Constructor - should get string and list of strings and save them under the fields question and answers accordingly.

print method - prints the question in the format '[?] {question}'
For example, if the question is 'Are you experienced programmer?', the method should print '[?] Are you experienced programmer?'

check method - returns True if input string (the answer) included in answers field, otherwise False.
For example, for answers = ['yes', 'maybe'] if check('yes') return True, if check('nope') return False
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
        

# Test Cases
obj1 = OpenQuestion("Are you happy today?", ["Yes", "ye", "Y", "yes!"])
print(f"{obj1.question}\n{obj1.answers}")
'''
Are you happy today?
Yes,ye,Y,yes!
'''

obj2 = OpenQuestion("Are you happy today?", ["Yes", "ye", "Y", "yes!"])
obj2.print()
print(obj2.check("ye"))
print(obj2.check("no"))
'''
[?] Are you happy today?
True
False
'''

obj3 = OpenQuestion("How hard is code learning?", ["not hard at all", "with Coddy it's easy"])
print(obj3.check("not hard at all"))
print(obj3.check("with Coddy it's easy"))
'''
True
True
'''