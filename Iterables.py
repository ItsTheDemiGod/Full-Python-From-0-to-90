# iterables = an object / collection that can return its elements one at a time or
# in simple words accessing every element in a collection one at a time


numbers=[1,2,4,5,6,7,6]
for num in numbers:
    print(num,end=" ")
print()

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit,end=" ")
print()

name = "Nithya"
name = set(name)
for char in name:
    print(char,end=" ")
print()


dictionary = {"A" : "demian","B" : "Nithya" , "C" : "Robert"}
for key,value in dictionary.items():
    print(f"{key} is {value}")


