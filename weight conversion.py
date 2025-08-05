# kg --> lbs (you multiply the weight by 2.207)
# lbs --> kgs (you divide the weight by 2.207)

weight = float(input("Enter your weight(in kg or lbs) : "))
unit = input("Enter your unit(kg or lbs): ")

if unit == "kg":
    weight = weight /2.207
    print(f"your weight is{weight} kgs " )
elif unit == "lbs":
    weight = weight* 2.207
    print(f"your weight is{weight} lbs ")



