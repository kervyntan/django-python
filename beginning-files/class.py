class Student():
    planet = "Earth" # class object attribute, global
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

# attributes descibe the class - eg. name and gpa are characteristics of student

num = Student(name="Kervyn", gpa=4.0)
num2 = Student(name="jaiwei", gpa=3.5)
print(num.name)

class Agent():

    origin = "USA"
    
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

x = Agent('Jose', 12, 180)
print(x.weight)
x.weight = 200
print(x.weight)
        