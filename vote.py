DOB = int(input("Enter your Birth year: "))

Current_year = 2025
age = Current_year - DOB

print("Your age is:", age)

if age >= 18:
    print("Hey! You are eligible to vote.")
else: 
    print("Hey! You are NOT eligible to vote.")