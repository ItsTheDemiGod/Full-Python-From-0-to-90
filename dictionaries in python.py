#  dictionary = collection of {key:value} pairs
#  it is mutable, unordered, indexed by keys
#  created using { }

capital = { "USA" : "Washington DC" ,
            "France" : "Paris" ,
            "Germany" : "Berlin" ,
            "Italy" : "Rome",
            "India" : "Delhi"}
#print(capital)

#print(dir(capital)) # gives you a list of operations you can perform under dictionary

#print(capital["USA"]) # prints the value of USA
# if you think about it keys behaves as index and values behave as values


#print(capital["France"]) # ------\
#print(capital.get("Italy")) # ---/  behaves the same


#print("USA" in capital ) # checks whether USA is present or not


#if "USA" in capital:
#    print("i am right")
#else :
#    print("i am wrong")

#capital.update({"India":"Mumbai"}) # we put curly braces because its dictionary
#print(capital)


#capital.pop("Italy")
#print(capital)



#capital.clear() #  clears the whole dictionary

print(capital.keys()) # printing the keys of the dictionary
print(capital.values()) # printing the values of the dictionary

print(capital)
for key,value in capital.items():
    print(f"{key}:{value}")