# learning about the special methods in python and how to access it 
class Book:
    def __init__(self,title, author, pages):
        print('A book is created')
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages
    def __del__(self):
        print('A book is destroyed')
