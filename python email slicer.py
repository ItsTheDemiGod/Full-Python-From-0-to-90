# python email slicer

email = "brocode@gmail.com"

print(email)
print(type(email))
print(len(email))
print(email[::])
print(email[:5])
print(email[email.index('@')+1:]) # note: [int:int:int] --> this value should be integer
print(email[-4:])
print(email.find("@"))

# all the operations we performed earlier on string methods we can perform it here
