import numpy as np
from datetime import date

years=100

name = input("Give me your name: ")
print("Your name is " + name)
age = input("Hello " + name + ", can you please give me you age? ")
age_int=int(age)
print("You are " + age + " years old")
when = str(years - age_int + date.today().year)
print(name + ", you will turn 100 years old on the year " + when)
