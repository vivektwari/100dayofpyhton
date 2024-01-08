print("welcome to gaint_wheel")

hieght=int(input("Enter your heigt in cm "))
age = int(input("Enter your age "))
bill=0
if hieght >= 120:
  print("You are eligible to  ride ")

  if age <=12:
    bill = 50
    print("plase pay 50rs ")
    
  elif age <18:
    bill = 70
    print("plase pay 70rs ")
  elif age >=18:
    bill = 100
    print("plase pay 100rs ")
  elif age <=45 and <=55:
    print("Ist free for you Guys")
  want_photo = input("If want photo? enter Y or N ")
  if want_photo == "Y":
    bill = bill + 10
    print(f"your final bils {bill}rs")
else:
  print("you are not eligible for the ride")

