# format specifier is the way how we want to represent our outputs
# the following are the ways in which we can represent the outputs :
# 1. .nf - digits after decimal places
# 2. n  - padding
# 3. > ,< , ^ - left justified , right justified or centre justified
# 4. +        - represent the values with respective signs


price1 = 3.14159
price2 = -987.65324
price3 = 12.22343


print(f" price 1 is {price1:.2f}") # .2f refers to having 2 digits after decimal places
print(f" price 2 is {price2:.2f}")
print(f" price 3 is {price3:.2f}")

print(f" price 1 is {price1:10}") # total length of the digits is 10 , places are filled with space
print(f" price 2 is {price2:.10}")
print(f" price 3 is {price3:.10}")


print(f" price 1 is {price1:010}") # the spaces are filled with zero if you put 0 before 10
print(f" price 2 is {price2:.010}")
print(f" price 3 is {price3:.010}")

print(f" price 1 is {price1:<10}") # the spaces have been left justified
print(f" price 2 is {price2:.<10}")
print(f" price 3 is {price3:.<10}")

print(f" price 1 is {price1:>10}") # the spaces have been right justified
print(f" price 2 is {price2:.>10}")
print(f" price 3 is {price3:.>10}")


print(f" price 1 is {price1:^10}") #the spaces have been centre justified
print(f" price 2 is {price2:.^10}")
print(f" price 3 is {price3:.^10}")

print(f" price 1 is {price1:+}") # the values are with their signs
print(f" price 2 is {price2:+}")
print(f" price 3 is {price3:+}")



