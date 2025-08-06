# default arguments in functions are default values for certain parameters
# for a function to make the function more flexible
# note we have to set the default values during the creation of a Function
# there are 4 kinds of  Arguments
# 1. positional
# 2. Default
# 3. keyword
# 4. Arbitary

def bday(name,age=21):
    print(f"happy birthday to {name}")
    print(f"you are {age} years old")
bday("demian") # here even if we dont have the value for age we have already set
# the default value to 21 so its ok


def net_price(list_price,discount=0,tax=2): # ----> default argument
    return list_price*(1-discount)*(1+tax)
print(net_price(230))



# suppose if you do wanna put the values the new values are used instead of the defaults

print(net_price(230,5,4))


import time
def count(end,start=0):
    for x in range(start,end+1):# note here its end+1 because in for loop the ending point is
        print(x)               # is exclusive so if we dont put +1 the last sec wont be counted
        time.sleep(1)
    print("done")
count(10)


