# calculator program to understand if else statements
num_1 = int(input("enter the first number"))
num_2 = int(input("enter the second number"))
operator = input("enter the operator(+,-,*,/,^): ")

if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
elif operator == "^":
    print(num_1 ** num_2)
print(num_1, num_2, operator)