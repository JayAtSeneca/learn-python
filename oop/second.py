class Dog:
    #class object attribute
    species = 'mammal'
    # it is known as constructor and self is the instance of the object itself
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    # method is a function inside of the class
    def bark(self):
        print('WOOF!')