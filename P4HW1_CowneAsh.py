# P4HW1 
#11/12/2024
#Ash Cowne
#Assignment assess student ability to edit and enhance exiting programs

# varables
grade = ""
score_list = []
lowest_score = 0
average_score = 0
num_log = 0
score_placeholder = 0
#Getting the score from the user.
score = int(input("How many score do you want to enter? "));

# While loop to get the score numbers from the user.
while score > num_log:
    # Adding the num_log takes it out of a infinate loop and lets the user know what score number their on.
    num_log += 1
    score_placeholder = float((input(f"Enter Score #{num_log}: ")));
    # If else stament to check if the score is valid and letting the user try again.
    if (score_placeholder >= 0) & (score_placeholder <= 100):
            score_list.append(score_placeholder)
    else:
        print("INVALID Score entered!!!");
        print("Score should be between 0 and 100");
        # So the program do'snt skip the number you put a invaled score on and so you can try again.
        num_log -= 1

# Caculations for lowest and average.
lowest_score = min(score_list)
score_list.remove(lowest_score)
average_score = sum(score_list) / len(score_list)

# If else statments to get the grade number.
if (average_score >= 100) & (average_score > 90):
    grade = "A"
elif (average_score >= 80) & (average_score < 90):
    grade = "B"
elif (average_score >= 70) & (average_score < 80):
    grade = "C"
elif (average_score >= 60) & (average_score < 70):
    grade = "D"
elif (average_score >= 50) & (average_score < 60):
    grade = "E"
else:
    grade = "F"


# Printing out the info for the user.
print("-------------------------Results-------------------------");
print(f"Lowest Score        : {lowest_score}");
print(f"Modified List        : {score_list}");
print(f"Scores Average     : {average_score}");
print(f"Grade                    : {grade}");
print("---------" * 7);












