import random  # WE USE random module to generate random number in python

#num = random.randint(0,10) print a random integer from 0 to 10
#num = random.random() Returns a random float in the range [0.0, 1.0).
#num = random.randrange(0,10,2) # Returns a randomly selected element from range(start, stop, step).
#random.seed(1) # Initializes the random number generator. Use the same seed for reproducible results.
#print(random.random())

numbers =  [1,2,4,5,6]
random.shuffle(numbers) # shuffle the values
print(numbers)