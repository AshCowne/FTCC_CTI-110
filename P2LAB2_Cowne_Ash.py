# Ash Cowne
# 10/10/2024
# P2LAB2

# A program that creats a dictoranry where the key and value pairs are given.

# Dictornay
car_facts = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Sulverado":26,}

# Making a variable for all the keys and printing out the keys for the user.
keys = car_facts.keys()
print(keys);
print("");

# Getting User input to get the varible to select from the dictoranry.
car_name = input("Enter a vehicle to see it's mpg:");
print("");

# Printing out the facts of from the Users output.
print(f"The {car_name} gets {car_facts[car_name]}.");
print("");

# Getting how far the User will drive the car.
miles = float(input(f"How many miles will you drive the {car_name}?  "));
print("");

# Caulating how many gallons the User output will use up and printing the answer.
caculations_for_gas = miles/car_facts[car_name]
print(f"{caculations_for_gas:.2f} gallon(s) of gas are needed to drive the {car_name} {miles} miles.")
