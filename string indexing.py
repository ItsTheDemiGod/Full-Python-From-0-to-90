# string indexing refers to slicing the string and the accesing it .
# here we access the particular elements of the string without accessing the whole
# string
# [start:end:step]
credit_card = "1234-5678-9012"
print(credit_card)
print(len(credit_card)) # gives the length of the string
print(credit_card[:5]) # the starting index is inclusive and the ending index is exclusive
print(credit_card[5:9]) # accessing elements from 5 to 9
print(credit_card[-1]) # accessing the last element
print(credit_card[::]) # accessing all the elements
print(credit_card[::2]) # printing everything with a 2 step gap

last_digit = credit_card[-4:]
print(f'xxxx-xxxx-{last_digit}')