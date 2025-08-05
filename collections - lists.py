# collections = it is a single variable storing multiple variables of the same datatype
# in here we will study 3 kinds of collections
# 1. lists[] = ordered, changeable, duplicates are OK
# 2. sets{} = unordered, immutable, add/ removes are OK , n duplicates
# 3. tuple() = ordered and unchangeable , duplicates are Ok , faster


# lists

fruits = ["apple", "banana", "cherry","kiwi" , "mango"]
# fruits.reverse()
#fruits.sort()
#fruits.append("orange")
#fruits.append("kiwi")
#fruits.remove("apple")
#fruits.pop()
# slicing a list

#print(fruits[::])
#print(fruits[-1])
#print("apple" in fruits)
#print(fruits[0])
#fruits.insert(5,"guava")
fruits.append("apple")
print(fruits.count("apple"))
print(fruits)
