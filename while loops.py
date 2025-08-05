# while loops = executes a set of codes again and again as long as conditions remain
#               remain true
"""""
name = input("Enter your name: ")

while name == "":
    print("enter your name again !")
    name = input("Enter your name: ")
print(f"Your name is {name}")
"""



age = input("Enter your age: ")
while age == "":
    print("enter your age again !")
    age = input("Enter your age: ")

while int(age) < 0 or int(age) > 100 :
    print("age cant be less than zero")
    age = input("Enter your age: ")

print(f"Your age is {age}")



