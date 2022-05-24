class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('Subclass must implement abstract method')
class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + 'Says Woof!'
class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + 'Says meow!'
        