print("Welcome to the tip calculator.")
bill = input("What was the total bill?\n$")
people = input("How many people to split the bill?\n")
tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
given_tip = (int(tip) / 100)
bill_person = (int(bill) / int(people))
calculation_per_person = bill_person * given_tip + bill_person

print(f"Each person should pay: ${calculation_per_person:.2f}")
