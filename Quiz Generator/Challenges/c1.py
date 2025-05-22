'''
Question:-

Example of abstract class with two abstract methods,

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def bar(self, a, b):
        pass

Challenge

Create abstract class named Question with the following methods:

print- abstract method which takes no input.
check- abstract method which takes string (the answer types by the user) as input.
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

obj = Question()