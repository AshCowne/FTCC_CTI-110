# Ash Cowne
# 9/26/2024
# P1HW2
# A program to do basic math on the numbers that are entered.


# Tell's the user the point of the program.
print("Enter infomation to this program to caculate and display your travel expensise.");

# Asking user for infomation to set the varibles to.

buget = float(input("Enter Buget: "));
print("");
destination = input("Enter yout travel destination: ");
print("");
gas = float(input("How much do you think you'll spend on gas: "));
print("");
housing = float(input("How much do you think you'll spend on housing/hotel/accomodations/airbnb/ect..: "));
print("");
food = float(input("How much do you think you'll spend on food and beverages: "));


# Caculating the expensives.
remaing_balance = float( buget - gas - housing - food );

# Showing the results as well as rounding the answers to make it look like money.
print("");
print("");
print("");
print("-----------------Travel Expenses--------------");
print("Location:", destination)
print("Initial Buget:", round(buget,2));
print("");
print("Initial Buget Structure");
print("Gas:", round(gas,2));
print("Accomodation:", round(housing,2));
print("Food + beverages", round(food,2));
print("");
print("Balance:", round(remaing_balance,2));

# Adding comments on user buget value.
if remaing_balance > 0 :
# If they have enough money, tell them to have a great trip.
    print("Have a great trip!");
elif remaing_balance < 0 :
# If they don't have enough money, tell user that they should do something else as the trip won't go as play with their buget.
    print("This trip isn't feasible, try to save up or spend more on the buget for the trip.");
else:
# Giving advace to the user so they watch out on their expenses as they don't have extra money.
    print("Your at 0, try to save up more money, spend more on the buget for the trip, or be carfull on how much you stend. But if your still going, have a great trip!");
