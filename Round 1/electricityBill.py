# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


# Taking Units Consumed as Input
units = int(input("Enter Units Consumed: "))#removed ";" 'will cause syntax error' and changed the input type to int

totalBill=1
# Calculating Bill Based on Slabs
if units <= 100:#changed the limit so that it can be calculate from 1to 100
    totalBill = (units * 3)#removed ";" 'will cause syntax error'

elif units <= 200:
    totalBill = (100*3 + (units-100*5))#removed ";" 'will cause syntax error'

elif units <= 300:
    totalBill = 100*3 + 100*5 + units-200*7#removed ";" 'will cause syntax error'

else:
    totalBill = 100*3 + 100*5 + 100*7 + units-300*10#removed ";" 'will cause syntax error'

# Displaying the Final Bill
print(f"Total Electricity Bill: {totalBill}")#removed ";" 'will cause syntax error'