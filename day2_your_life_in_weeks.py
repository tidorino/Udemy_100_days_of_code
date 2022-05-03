age = input("What is your current age?")
age_left = 90 - int(age)
year = 365 * age_left
week = 52 * age_left
month = 12 * age_left


print(f"You have {year} days, {week} weeks, and {month} months left.")
