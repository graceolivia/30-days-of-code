from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook():
    def __init__(self, title, author, price):
        Book.__init__(self, title,author)
        self.price = price
        def display():
            print("Title: ".format(self.title))
            print("Author: ".format(self.author))
            print("PRice: ".format(self.price))

title=input()
