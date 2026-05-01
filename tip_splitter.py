'''
Sadie Crandall
IS 303 - AO1

Tip Splitter
This program calculates the amount of the bill 
each person has to pay, including the tip.

Inputs: 
- Restaurant name (string)
- Total bill amount (float)
- Tip percentage (float)
- Number of people splitting the bill (integer)

Processes:
-calculates the total bill including the tip ( bill * (1 + tip%/100))
-calculates the amount each person has to pay(per person = total / people)

Outputs:
- Total bill including tip (float)
- Amount each person has to pay (float)
- Prints the restaurant name, total bill including tip, and amount each person has to pay in a formatted manner.

'''

restaurant_name = input("Enter the restaurant name: ")
total_bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
number_of_people = int(input("Enter the number of people splitting the bill: "))

total_with_tip = total_bill * (1 + tip_percentage / 100)
amount_per_person = total_with_tip / number_of_people

print("---")
print(f"Restaurant: {restaurant_name} | Total Bill: ${total_bill:.2f} | Tip: {tip_percentage}% | People: {number_of_people}")
print(f"Total bill including tip: ${total_with_tip:.2f}")
print(f"Amount each person has to pay: ${amount_per_person:.2f}")
print("---")