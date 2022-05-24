#basic syntax of python classes/objects
class Dog:
    # it is known as constructor and self is the instance of the object itself
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

# how to pass: my_dog = Dog(breed='lab', name='sam')
