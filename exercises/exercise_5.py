# Exercise 5
# Your solution comes here

num1 = int(input("Enter an integer:  "))
num2 = int(input("Enter an integer:  "))

# print(max(num1,num2))
max_value = (num1 + num2 + abs(num1-num2)) // 2

print(max_value)