'''
Print Results

Let's deal with the quiz results, and print them.


Challenge:-
Write a method print_results inside Quiz class which gets list of boolean as input (True means the ith question was answered correctly) and prints the result in specific format.

Check out the test cases to understand the format!
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
    
    def print_results(self, results):
        self.score = 0
        self.checks = []

        for i in range(len(results)):
            if results[i]:
                self.checks.append("Pass")
                self.score += 1
            else:
                self.checks.append("Fail")
        
        print(f"Your score is {self.score}/{len(results)}\n")
        
        for i in range(len(self.checks)):
            print(f"[{i+1}] {self.checks[i]}")
            

obj1 = Quiz([True, False, True])
obj1.print_results([True, False, True])
'''
Your score is 2/3

[1] Pass
[2] Fail
[3] Pass
'''

obj2 = Quiz([True, True, True, True, True])
'''
Your score is 5/5

[1] Pass
[2] Pass
[3] Pass
[4] Pass
[5] Pass
'''
obj3 = Quiz([True, False, False, True, True])
'''
Your score is 3/5

[1] Pass
[2] Fail
[3] Fail
[4] Pass
[5] Pass
'''