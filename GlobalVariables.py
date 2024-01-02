x ="Awesome"

def myfunc():
    print("Python is "+x)

myfunc()

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 