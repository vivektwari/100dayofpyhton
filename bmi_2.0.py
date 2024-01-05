print("welocome to bmi calculator")

w = int(input("Enter you weight in kg  "))
h = float(input("Enter your height in meter "))
bmi = w / (h * h)
if bmi < 18.5:
  print(f"bmi is{bmi}drunk your milk")

elif bmi < 25:
  print(f"your bmi is{bmi} you are the man")

elif bmi > 25:
  print(f"oyurt bmi is {bmi}you are a pig")





