# Ash cowne
# 10/24/2024
# P3HW1


# In this assignment you are building on P2HW2_Lists. Only for this assignment, you are given a partial program with bugs. You are to correct the program and complete it.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "));
mod_2 = float(input("Enter grade for Module 2: "));
mod_3 = float(input("Enter grade for Module 3: "));
mod_4 = float(input("Enter grade for Module 4: "));
mod_5 = float(input("Enter grade for Module 5: "));
mod_6 = float(input("Enter grade for Module 6: "));

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
grade_sum = sum(grades)
avg = grade_sum / len(grades)

# Variable for grade letter.
grade_letter = ""

# determine letter grade for average

if avg >= 90.00 :
    grade_letter = "Your grade is: A"
elif (avg >= 80.00) & (avg <= 89.99) :
    grade_letter = "Your grade is: B"
elif (avg >= 70.00) & (avg <= 79.99) :
    grade_letter = "Your grade is: C"
elif (avg >= 60.00) & (avg <= 69.99) :
    grade_letter = ("Your grade is: D");
elif (avg >= 50.00) & (avg <= 59.99) :
    grade_letter = "Your grade is: E"
else:
    grade_letter = "Your grade is: F"

# TO DO: finish this
print()

print("----------------Results---------------");
print(f"{'Lowest Grade:':<30} {low}");
print(f"{'Highest Grade:':<31} {high}");
print(f"{'Sum of  Grade:':<31} {grade_sum}");
print(f"{'Average:':<34} {avg:,.2f}");
print("---"*23);
print(grade_letter)
