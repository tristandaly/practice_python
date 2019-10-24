list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_three = []

for number in list_one:
  if number in list_two:
      list_three.append(number)

list_four = list(dict.fromkeys(list_three))

print(list_four)
