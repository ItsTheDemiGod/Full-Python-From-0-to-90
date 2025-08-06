# keyword arguments = it is an argument that is precede by an identifier
#                     that helps with the readibility , order of arguments doesn not matter
#                     if the keyword argument is present otherwise it does matter



# positional Arguments

def hello(first,middle,last):
    print(f"hello {first} {middle} {last}")
hello("Mr","Raj","Kumar")

# in the above example the position of the arguments matters otherwise the name
# will be wrong

hello("MR" , last="Kumar" , middle = "Raj") # here the order of the arguments does not maatter
# because we are using keywords arguments



