# Ash Cowne
# 11/14/2024
# P4LAB2
# USe while loop and for loop together.

# Varible to run program agian

run = "yes"

while run.lower() != "no":
    # Get a integer from user.
    num = int(input("Enter and integer: "))

    if num >= 0:
        #Multiplying the inputed integer from 1-12 and displaying it.
        for muliply in range(1,13):
            print(f"{num} * {muliply} = {num * muliply}")
    else:
        print("This program does not handle negative values")
        
    run = input("Would you like to run the program again? Enter yes or no: ")

#Showing the loop and program is done.
print("Program is ending......")
