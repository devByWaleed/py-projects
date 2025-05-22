'''
Final Touch


Challenge:-
Put everything together.

In the start method in Quiz, count the number of results and call print_results method from last lesson in the end.

Check the test cases, for examples.
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

        self.results = []

        for i in self.questions:
            i.print()
            print()

            user_ans = input("[+] ")
            print()
            answer = i.check(user_ans)
            self.results.append(answer)

        self.print_results(self.results)
        
    
    def print_results(self, results):
        self.score = 0
        self.checks = []

        for i in range(len(results)):
            if results[i]:
                self.checks.append("Pass")
                self.score += 1
            else:
                self.checks.append("Fail")
        
        print(f"Your score is {self.score}/{len(results)}")
        
        for i in range(len(self.checks)):
            print(f"[{i+1}] {self.checks[i]}")
        print()


obj1 = Quiz([OpenQuestion('How are you?', ['Great!', 'Amazing']), YesNoQuestion('Are you happy?', True)])
obj1.start()
# Great!
# yes
'''
[?] 'How are you?'

[+] 

[?] 'Are you happy?' (yes/no)

[+] 

Your score is 2/2

[1] Pass
[2] Pass
'''

obj2 = Quiz([MultiOptionsQuestion('???', ['this', 'that', 'or else'], 2)])
obj2.start()
# 1
'''
[?] '???'

[1] this
[2] that
[3] or else

[+] 

Your score is 0/1

[1] Fail
'''