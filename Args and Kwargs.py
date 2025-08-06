# args  = allows you to pass multiple non non-key arguments
#  **Kwargs** = allows you to pass multiple key word arguments
#   * is the unpacking operator



"""def add(x,y):
    return x+y
add(1,2,3)
 the above code won't work because we are passing 3 arguments when it has place for
only has 2 arguments
"""

# now with the help of * args we can add multiple argument to non-keyword argument


def add(*args): # here arg is a tuple and will have multiple values inside it
    total = 0 # here only the Unpacking operator matters and not the name
    for arg in args:
        total = total + arg
    return total
print(add(1,2,4,5))


def name(*names):
    for name in names:
        print(name,end = " ")

name("demian" , "Xaxa")

# using ** Kwargs --> adding multiple values to keyword arguements

def address(**address):
    for key,value in address.items():
        print(f"{key}: {value}")

address(country="india" , state = "jharkhand" , city = "ranchi" ,pincode = 834001)
# if you want you can add more arguments in the above function like see below.


address(country="XYX",state="fnwf",city="fwef",pincode=13131,post="wfwf",road="wfwfw")

# so you can add as many arguments as you want.



