from mypackage.mysubmodule import my_sub_func

class Circle():

    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def perimeter(self):
        return 2 * self.radius * Circle.pi

mycircle = Circle(radius = 20)
print(mycircle.perimeter())


class Book():
    def __init__ (self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__ (self): # method used to generate string representation in each instance
        return f"{self.title} is the best book by {self.author}"
    
    def __len__ (self):
        return self.pages

mybook = Book('Python Rocks!', 'Kervyn', 150)
print(mybook) # for __str__ use
print(len(mybook)) # for __len__ use

my_mod_instance = UsefulClass("eat shit")
my_mod_instance.report()

my_sub_func()