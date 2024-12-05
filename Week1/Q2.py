# write a python program to delete the second last digit and print this. If input is 267 then output is 2
digit = int (input("Enter a number: ")) 
last_digit = digit / int(10)
second_last_digit = int(last_digit) % int(10)

print("The second last digit is:", second_last_digit)

# Another better approach
n=input("enter a number : ")
print(n[-2])