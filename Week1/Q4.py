# write a python program to read a number and find their product after exchanging last digits. if inputs are 348 and 31 then output is 12958 (341*38).

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

last_digit_num1 = num1 % 10
last_digit_num2 = num2 % 10

new_num1 = (num1 // 10) * 10 + last_digit_num2
new_num2 = (num2 // 10) * 10 + last_digit_num1

product = new_num1 * new_num2

print("The product of the numbers is:", product)
