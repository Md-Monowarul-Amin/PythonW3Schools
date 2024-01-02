a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a) 

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a)) 

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") 

txt = "The best things in life are free!"
print("expensive" not in txt) 

#### Slicing Strings
b = "Hello, World!"
print(b[2:5]) 
print(b[:5])
print(b[2:])