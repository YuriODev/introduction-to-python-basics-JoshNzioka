# Exercise 3
hours =00
min = 00
sec = 00

sec_past = int(input())

sec = sec_past
if sec_past >= 60:
  min = sec_past//60
  sec = sec_past % 60
if min >= 60:
  hours = min //60
  min = min%60



newtime = (f"{hours}:{min:02d}:{sec:02d}")

print(newtime)