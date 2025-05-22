'''
Yes/No Question


Challenge:-
Create class YesNoQuestion which inherits from Question and implements constructor and the methods print and check from Question class.

 

Constructor - should get string and boolean and save them under the fields question and answer accordingly.

 

print method - prints the question in the format '[?] {question} (yes/no)'

For example, if the question is 'Are you experienced programmer?', the method should print '[?] Are you experienced programmer? (yes/no)'

 

check method - returns True if input string is 'yes' and answer (class field) is True or if input string is 'no' and answer is False, otherwise False.
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

        
# Test Cases
obj1 = YesNoQuestion("Are you experienced programmer?", True)
print(f"{obj1.question}\n{obj1.answer}")
'''
Are you experienced programmer?
True
'''

obj2 = YesNoQuestion("Are you experienced programmer?", True)
obj2.print()
'''
[?] Are you experienced programmer? (yes/no)
'''

obj3 = YesNoQuestion("Are you tired?", False)
print(obj3.check('yes'))
print(obj3.check('no'))
print(obj3.check('')) 
'''
False
True
False
'''