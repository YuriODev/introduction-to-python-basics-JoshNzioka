# Exercise 3
hours =00
min = 00
sec = 00

sec_past = int(input())

hours = (sec_past//3600) %24
min = (sec_past % 3600)//60
sec = (sec_past %3600) %60




newtime = (f"{hours}:{min:02d}:{sec:02d}")

print(newtime)