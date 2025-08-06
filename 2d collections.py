# 2-d collections are the collections having rows and Columns

items = [["A","B","C"],
         ["D","E","F"],
         ["G","H","I"]]
# the Above is a 2d Lists having some rows and columns
print(items[1][2]) # this prints the 1st row and 2 column items
for item in items :
    for x in item :
        print(x,end = " ")
    print()


 # ------- this is the concept of 2d lists------------#

fruits =    ["apple", "banana", "cherry"]
vegetables =["carrot","cabbage" , "celary"]
meats =     ["chicken" , "fish" , "beaf"]


groceries = [fruits,vegetables,meats]# this is the process of nested lists



print(groceries)
print(groceries[0][1])
for items in groceries:
    for x in items:
        print(x , end = " ")
    print()

# Making a numpad

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for item in num_pad:
    for num in item:
        print(num,end = " ")
    print()
