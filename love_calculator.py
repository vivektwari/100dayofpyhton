print("Welcome To Love Calculator")

personA = input("Person_A Enter your name ")
personB = input("Person_B Enter your name ")

combine_person = personA + personB
lower_case = combine_person.lower()

t = lower_case .count("t")
r = lower_case .count("r")
u = lower_case .count("u")
e = lower_case .count("e")

first_digit = t+r+u+e

l = lower_case .count("l")
o = lower_case .count("o")
v = lower_case .count("v")
e = lower_case .count("e")

second_digit = l+o+v+e

percentage = int(str(first_digit)+ str(second_digit))

if (percentage < 10 or percentage > 90):
  print(f"Your percentage is Good {percentage}")
elif (percentage >= 35 and percentage <=55):
 print(f"Your perentage is  great  {percentage}")
else:
  print(f"Your percentage is {percentage} ")