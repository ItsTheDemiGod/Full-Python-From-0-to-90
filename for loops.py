# for loops = executes a block of codes a fixed number of times
# you can iterate over a range , string , sequence etc


for x  in range(1,11 ,2): # here 1 is the starting index(inclusive) and 11 is the ending index
    print(x)         # which is exclusive and 2 is the step
                     # x is called the counter which is used to store the iterables

# if you want to print them in a single line you do this

for x in range(1,11):
    print(x,end= " ")
print()

# printing the elements in reversed order

for x in reversed(range(1,11)):
    print(x,end= " ")
print()

for x in (range(11,0,-1)):
    print(x, end=" ")
print()



# using a break statement and continue

for x in range(1,11):
    if x % 2 == 0:
        break
    else :
        print(x)



