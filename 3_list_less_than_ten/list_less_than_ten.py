numbered_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
new_new_list = []

number_input = int(input("Number: "))

for number in numbered_list:
    if number < 5:
        new_list.append(number)
        new_new_list.append(number)
    elif number < number_input:
        new_new_list.append(number)

print(new_list)
print(new_new_list)
