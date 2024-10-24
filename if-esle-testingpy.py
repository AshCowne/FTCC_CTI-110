# Ash cowne
# 10/24/2024
# If-else statemts


num1 = 1
num2 = 1
life_stage = ""

'''
if num1 == num2 :
    print(f"{num1} is equal to {num2}.");
elif num1 > num2 :
    print(f"{num1} is greater than {num2}.");
else:
    print(f"{num1} is not greater than {num2}.");
'''
# Get input from user
age = int(input("Enter an age: "));

'''
if age > 65 :
    life_stage = "Senior"
    print(life_stage)
elif age > 17 :
    life_stage = "Adult"
elif age > 12 :
    life_stage = "Teenager"
elif age > 5 :
    life_stage = "Child"
elif age > 0 :
    life_stage = "Baby"
else:
    life_stage = "Stop. You do not exist yet. Or you mistiped, either way start again."


print(f"You are {age} years old and you are a {life_stage}");
'''
if age >= 0 & age <= 5 :
    life_stage = "Baby"

if age >= 6 & age <= 12 :
    life_stage = "Child"

if age >= 13 & age <= 17 :
    life_stage = "Teenager"

if age >= 18 & age <= 65 :
    life_stage = "Adult"

if age >= 66 :
    life_stage = "Senior"

print(f"You are {age} years old and you are a {life_stage}");
