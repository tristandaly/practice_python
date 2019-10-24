number_input = int(input("Number: "))

candidate_list = range(1, number_input + 1)
divisor_list = []

for number in candidate_list:
    if number_input % number is 0:
        divisor_list.append(number)

print(divisor_list)
