#learning about inheritance concept in python
class Animal:
    def __init__(self):
        print('Animal Created')
    def whoAmI(self):
        print('Animal')
    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    def whoAmI(self):
        print('I am a dog ')
    def eat(self):
        print('I am eating!')

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
    def whoAmI(self):
        print('I am a cat')
    def eat(self):
        print('I am eating(CAT)')