class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 
    
x = Student("John", "Doe")
x.printname()

