'''Day-2 : Tip Calculator'''

# Total Bill string converted into int
totalBill = float(input("What was the total bill: $"))

# Split bill
splitBill = int(input("How many people to split the bill: "))

# Tip Percentage
tipPer = float(input("What percentage tip would you like to give (10, 12, or 15): "))

# Calculate each person cost
addTip = (tipPer * totalBill) / 100
afterTipTotal = totalBill + addTip
perPersonCost = round((afterTipTotal / splitBill),2)

# Result ouput
print(f"Each person should pay: ${perPersonCost}")