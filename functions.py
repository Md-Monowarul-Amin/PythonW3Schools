def my_function(fname):
  print(fname + " Refsnes")

def my_function():
  print("Hello from a function")

def my_function(**kids):
  print("The youngest child is " + kids['a'])

my_function(a="Emil", b="Tobias", c="Linus") 
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus") 
