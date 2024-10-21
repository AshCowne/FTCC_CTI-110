# Ash Cowne
#10/17/2024
#P2HW2
#Assignment assess student understanding of Lists


#Creating varibles for the list.
print("Enter the test grades below.");
m1 = float(input("Modul 1: "));
m2 = float(input("Modul 2: "));
m3 = float(input("Modul 3: "));
m4 = float(input("Modul 4: "));
m5 = float(input("Modul 5: "));
m6 = float(input("Modul 6: "));

#Creating empty list.
test_grades = [m1, m2, m3, m4, m5, m6]

#Varible for calculating average.
average = sum(test_grades) / len(test_grades)

#Printing statments.
print("----------------Results---------------");
print(f"{'Lowest Grade:':<30} {max(test_grades)}");
print(f"{'Highest Grade:':<31} {min(test_grades)}");
print(f"{'Sum of  Grade:':<31} {sum(test_grades)}");
print(f"{'Average:':<34} {round(average,2)}");
print("---"*23);
