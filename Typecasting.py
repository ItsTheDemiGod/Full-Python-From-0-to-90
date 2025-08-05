# typecasting = changing the datatype(nature) of the variable into string, float, integer, or boolean
# there are Two types of Typecasting:
#1. Implicit
#2. Explicit
# Implicit Typecasting
name = "Demian"
print(type(name)) # used to know the datatype of the variable

age = 20
print(type(age))
age = float(age) # int ---> float
print(type(age))
print(age)
age = str(age) #int ---> string
print(type(age))
boolean=True
print(type(boolean))
boolean = str(boolean) # boolean ---> string
print(type(boolean))



# explicit ---> indirect typcasting

x = 4
y = 2
z =x/y
print(z)
print(type(z))
print(type(x))  # x,y --> integer but x/y ---> float. this is in indirect typecasting