# write a  python  program to print the sum of last two digits. If input is 13613 then output is 1 + 3  = 4

number = int(input("Enter a number: "))

last_digit = number % 10
second_last_digit = (number // 10) % 10

sum_of_last_two = last_digit + second_last_digit

print("The sum of the last two digits is:", sum_of_last_two)
