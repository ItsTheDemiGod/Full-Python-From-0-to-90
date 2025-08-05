# nested loops - it refers to loop within a loop
#a perfect example of nested loops is printing symbols

for x in range(1,11):
    for y in range(1,5):
        print(y, end=" ")
    print()



rows = int(input("Enter your rows: "))
columns = int(input("Enter your columns: "))
symbols = input("Enter your symbols: ")

for x in range(rows):
    for y in range(columns):
        print(symbols, end=" ")
    print()