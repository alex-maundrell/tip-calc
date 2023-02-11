# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# Enter bill amount: $
# How many people will be splitting the bill?
# How much would you like to tip? 10, 12 or 15?


bill = float(input("What is the bill amount?\n"))
num_of_persons = int(input("How many people are splitting the bill?\n"))
tip_amount = float(input(
    "How much would you like to tip? 12, 15 or 20%? Please enter digits only\n"))

tip = bill * (tip_amount / 100)
total = bill + tip
total_each = total / num_of_persons

print(f"Each person should pay: ${total_each:.2f}")
