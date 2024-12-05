# write a python program to delete the last digit and print this. If input is 13613 then output is 3
digit = int (input("Enter a number: ")) 
last_digit = digit % 10

print("The last digit is:", last_digit)
