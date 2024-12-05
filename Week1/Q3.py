# write a python program to exchange the last two digits. if input 23617 then output is 23671

number = int(input("Enter a number: "))
last_digit = number % 10
second_last_digit = (number // 10) % 10

remaining_number = number // 100

new_number = remaining_number * 100 + last_digit * 10 + second_last_digit

print("The number after exchanging the last two digits is:", new_number)
