# Ash cowne
# 10/24/2024
# P3HW2
# Assignment assess student understanding of decision structures.
# Program to caculate a paychech based on overtime or no overtime.

# Creating varables and asking input from user.
employee_name = input("Please enter your name: ");
employee_hours = float(input("Please enter how many hours you've worked this week: "));
employee_pay_rate = float(input("Please enter your pay rate (Specifically how much you make a hour): $"));
true_employee_hours = employee_hours
employee_over = 0
employee_over_time_pay = 0
employee_noramal_pay = 0
employee_gross_pay = 0

# if statment to chech if employee has overtime and caculates the extra hours of overtime.
if employee_hours > 40 :
    employee_over = employee_hours - 40
    employee_hours = 40

# Caculations for how much a employee would get paid for normal hours, overtime hours, and thier gross pay.
employee_noramal_pay = (employee_hours * employee_pay_rate)
employee_over_time_pay = ((employee_over * employee_pay_rate) * 1.5)
employee_gross_pay = (employee_noramal_pay + employee_over_time_pay)
# Displaying employee infomation.
print("-----------------------------------------------------------------"*2);
print(f"{'Employee name:':<30} {employee_name}");
print();
print(f"{'Hours Worked':<31} {'Pay Rate':<31} {'Overtime':<31} {'OverTime Pay':<31} {'RegHour Pay':<31} {'Gross Pay':<31} ");
print(f"{true_employee_hours:<45.2f} ${employee_pay_rate:<36.2f} {employee_over:<42.2f} ${employee_over_time_pay:<42.2f} ${employee_noramal_pay:<35.2f} ${employee_gross_pay:<42.2f}");
print("-------"*40);
