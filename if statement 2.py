# one of the variants of if statement is the Nested If else and elif statement
# we will understand this with the help of an example

age =  int(input("Enter your age: "))

if age >= 18 and age <= 65:
    print("you are eligible to vote")
elif age < 0 or age > 100 :
    print("you are not alive ")
else:
    print("you are not eligible to vote")

# we can make this if statement as long as we want. its upto us