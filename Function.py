# funtions = A block of Reusable codes
# () we place braces after the funtion to invoke it


# normal ways of doing things
"""
print("happy birthday to you")
print("you are old today")
print("happy birthday to youu")

print("happy birthday to you")
print("you are old today")
print("happy birthday to youu")


print("happy birthday to you")
print("you are old today")
print("happy birthday to youu")
"""

#progammer's ways of doing things

"""def bday(): # ---> in the braces we can put parameters for the function
    print("happy birthday to you")

bday()
bday()
bday()
bday()"""


def bday(name,age):
    print(f"happy birthday to {name}")
    print(f"you are {age} years old today")

bday("demian",21)


# making a invoice

def invoice(name,amount,due_date):
    print(f"hello {name}")
    print(f"your bill of {amount:.2f} is Due {due_date}")

invoice("demian",21,"1/08/2020")



# making a small calculator

def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)

print(add(2,3))


