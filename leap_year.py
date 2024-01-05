print("welcome to leap year calculater")

ly = int(input("Enter a any year "))
if ly % 4 == 0:
  print("is a leap year")
  if ly % 100 !=0:
    print("is a leap year")
    if ly % 400 ==0:
      print("is a leap year")
    else:
      print("not a leap year")
else:
  print("not a leap year")
