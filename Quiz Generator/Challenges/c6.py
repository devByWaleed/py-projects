'''
Start:-

Challenge:-
Add the method start which gets no input to the class Quiz, the method will show questions (from questions field) and ask for input (answer) from the user.

Check the test cases to understand better the formatting, use the question method print.

Each input ask should start with '[+] ', check hint if you are not sure how to do it!

Note the spaces and new lines!
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

    def start(self):
        for i in self.questions:
            i.print()
            print()

            user_ans = input("[+] ")
            print()
            i.check(user_ans)


obj1 = Quiz([OpenQuestion('How are you?', ['Great!', 'Amazing']), YesNoQuestion('Are you happy?', True)])
obj1.start()
# user inputs
# Great!
# yes

'''
[?] 'How are you?'

[+] 

[?] 'Are you happy?' (yes/no)

[+]
'''

obj2 = Quiz([MultiOptionsQuestion('???', ['this', 'that', 'or else'], 2)])
# user input
# 1
obj2.start()
'''
[?] '???'

[1] this
[2] that
[3] or else

[+] 


'''