'''
Quiz:-

Challenge:-
Create a class Quiz.

The class will coordinate the questions.

 

Let's start by adding the constructor to Quiz, the constructor will get list of questions (Question class) and save it under the field named questions.
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


class Quiz():
    
    def __init__(self, quest_list):
        self.questions = quest_list


obj1 = OpenQuestion('How are you?', ['Great!', 'Amazing'])

obj2 = YesNoQuestion('Are you happy?', True)

'''
OpenQuestion('How are you?', ['Great!', 'Amazing'])
YesNoQuestion('Are you happy?', True)
'''

obj3 = MultiOptionsQuestion('???', ['this', 'that', 'or else'], 2)

'''
MultiOptionsQuestion('???', ['this', 'that', 'or else'], 2)
'''