import datetime

now = int(datetime.datetime.now().year)

name_input = input("Please enter your name: ")
age_input = input("Please enter your age: ")
int_age_input = int(age_input)
repeat_input = input("How many times do you want to see this?: ")
int_repeat_input = int(repeat_input)

for i in range(int_repeat_input):
    print((now - int_age_input) + 100)
    print()
