# P4HW2
#Ash Cowne
#11/12/2024
#Assignment assess student ability to edit and enhance exiting programs

# Put in P3HW2 Code.
# Have the first question have a statment for if Done is typed in terminate program else just repeaatthe program/ do it over agian.

# Varibles that have to be called before the while loop to use outside of it.
run = ""
total_employes = 0
total_overtimepay = 0
total_regularpay = 0
total_grosspay = 0

# While loop to see if the program will repeat again.
while(run.lower() != "done"):
    run = input("Enter employee's name or Done to terminate: ")

    if run.lower()  != "done":
        name = run
        hoursWorked = float(input("Enter number of hours worked: "))
        payRate = float(input("Enter employee's pay rate: "))

        #evalute overtime.
        if hoursWorked >40 :
            #calculate overtime
            overtimeHours = hoursWorked - 40
            #Calculate overPay
            overPay = overtimeHours * (payRate * 1.5)
            #calculate salary for reg hours
            regPay = 40 * payRate
            # calculate gross pay
            grossPay = regPay + overPay
        else:
            overPay = 0
            overtimeHours = 0
            regPay = hoursWorked * payRate
            grossPay = regPay

        # Display output
        print("-------------------------------------")
        print("Employee name:  ",name,"\n")
        print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
        print('--------------------------------------------------------------------------------------------------')
        print(f'{hoursWorked:<15}{payRate:<12}{overtimeHours:<12}{overPay:<20.2f}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')


        # Calculation total for employes and all the pay amounts.
        total_employes += 1
        total_overtimepay += overPay
        total_regularpay += regPay
        total_grosspay += grossPay
    else:
        break

print("")
# Printing statisticks
print("Total number of emplyees entered:  ",total_employes)
print(f"Total amount for over time:  ${total_overtimepay:.2f}")
print(f"Total amount paid for regular hours:  ${total_regularpay:.2f}")
print(f"Total amount paid for gross:  ${total_grosspay:.2f}")
