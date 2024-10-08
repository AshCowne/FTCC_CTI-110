# Ash Cowne
# 10/8/2024
# Using Python built-in libraries on date, time, month, and weekday, not a grade

# Import the datetime libary to use it in the program.
import datetime

# assong current date time to a varible.
time = datetime.datetime.now();
month = time.month
month_name = time.strftime("%B");
today = datetime.datetime.today();
weekday = datetime.datetime.today().weekday();
#todad_and_weakend = datetime

# Display date/time

print(f"The currnet date and time is {time}.");
print(f"The currnet month is {month}.");
print(f"The currnet month name is {month_name}.");
print(f"Today is {today}.")
print(f"The number of the week is {weekday}.")

# If-Else statement to determane the day of the week.
if weekday == 0:
    weekday_word = "Monday"
elif weekday == 1:
    weekday_word = "Tuesday"
elif weekday == 2:
    weekday_word = "Wensday"
elif weekday == 3:
    weekday_word = "Thursday"
elif weekday == 4:
    weekday_word = "Friday"
elif weekday == 5:
    weekday_word = "Saterday"
elif weekday == 6:
    weekday_word = "Sunday"
else:
    print("Invaled day of week!!!");
    weekday_word = "INVALID"

print(f"The day of the week is {weekday_word}")

