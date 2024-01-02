##AllowDuplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) 
print(thislist[-1]) 
print(thislist[1]) 
print(thislist[2:5]) 
print(thislist[:4]) 
print(thislist[2:]) 

#Insert
thislist.insert(2, "watermelon")
#Appendt
thislist.append("orange")
#remove
thislist.remove("banana")
#pop
thislist.pop(1)
print(thislist) 
# del thislist 
thislist.clear()
print(thislist)


##Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 



#Using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 

[print(x) for x in thislist] 
newlist = [x.upper() for x in thislist if x != "apple"] 
print(newlist)


### Sort List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) 


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) 

### Sort Descending
thislist.sort(reverse = True)


## Tuples
thisTuple = ("apple", "banana", "Cherry")
print(thisTuple)
print(len(tuple))

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) 


#Loop through the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) 




