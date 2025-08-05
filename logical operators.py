# logical operators in python have the same concepts as that of logical gates
# there are 3 Logical Operators that we are going to study in here:
# 1.AND = both the statements should be true then the output is true
# 2.Or = either of them should be true then the output is true
# 3.Not = if the statement is True then the Output is false or vice versa


temp = float(input("enter temperature :"))
is_sunny = True

if temp > 30 and temp < 100:
    print('its a sunny day ')
elif temp <30 and temp > 0:
    print("it a cold day ")
else :
    print('its a bad day ')

if is_sunny:
    print('its a sunny day ')

# Experiment
#  why dont you try using OR and Not operator and see what you get