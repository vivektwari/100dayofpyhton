#tip cal calculator



print("Welcome to tip calculator")

bill = int(input("what was the bill? $ "))
tip = int(input("ho much tip you would like to give? 7, 9 , 11? "))
people = int(input("how many people to split the bill?" ))
tip_as_percentage = tip / 100
total_tip = bill * tip_as_percentage
total_bill= bill + total_tip
bill_per_person = total_bill / people
final_bill = round(bill_per_person,2)
final_bill = "{:.2f}".format(bill_per_person)
print(f"each person should pay {final_bill}")
