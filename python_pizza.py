print("thans for chooseing pyhton pizza ")
size = input("what size do you want? S, M, or L ")
bill = 0
if size == "S":
  bill += 50
elif size == "M":
  bill += 120
else:
  bill += 180

extra_chatni = input("Do you wnat Extra chani? Y or N ") 
if extra_chatni == "Y":
  bill += 5

extra_chess = input("do you want extar chess? Y or N ")
if extra_chess == "Y":
  bill += 10
print(f"your bill is {bill}")