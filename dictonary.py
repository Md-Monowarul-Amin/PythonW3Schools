thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 

print(thisdict["brand"])
x = thisdict.keys()
y = thisdict.values()
print(x) #before the change
thisdict.pop("model")

##Loop through dictionary
for x in thisdict:
  print(thisdict[x]) 


### Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"]) 

