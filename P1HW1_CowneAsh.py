# Ash Cowne
# 9/24/2025
# P1HW1
# Get interger input from the user and preform math caculations.

# Display output to user.

print("----------------Calculationg Exponents----------------");
print();
print();

# Getting the integers.
base_value_integer = int(input("Enter an interger as the base value: "));
exponent_value_integer = int(input("Enter an interger as the exponent: "));
# Calculationg the exponents outcome.
integer_expmemts_out_come = int(base_value_integer **  exponent_value_integer);

# Showing the outcome of the input.
print(base_value_integer, "raised to the power of", exponent_value_integer, "is", integer_expmemts_out_come, "!!");
print();
print();


# Display output to user.
print("----------------Addition and Subtraction----------------");
print();
print();

# Getting integers.
starting_integer = int(input("Enter a starting integer: "));
adding_integer = int(input("Enter an interger to add: "));
subtracting_integer = int(input("Enter an interger to subtract: "));
# Calculating the outcome.
integer_add_subract_out_come = int(starting_integer + adding_integer - subtracting_integer );
print();
print();

# Shows the user the outcome.
print(starting_integer, "+", adding_integer,"-", subtracting_integer, "is equal to", integer_add_subract_out_come);

