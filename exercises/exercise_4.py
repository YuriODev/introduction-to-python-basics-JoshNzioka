# Exercise 4
# Your solution comes here
num = (input()
if len(str(num)) <4:
  num = str(num).zfill(4)
print(num)
  

if num[0] == num[3] and num[1] == num[2]:
    print(1)
  
else:
    print(0)