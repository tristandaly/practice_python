num = int(input("Number: "))

if num % 2 is 0:
    if num % 4 is 0:
        print("Even! And a multiple of 4!")
    else:
        print("Even!")
else:
    print("Odd!")

check = int(input("Another Number: "))

if num % check is 0:
    print(str(check) + " divides evenly into " + str(num) + "!")
else:
    print("Division with both numbers shows a remainder of " + (str(num % check)) + "." )            
