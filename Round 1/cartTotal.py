#there are ";" in the end of every line but it is used in c and c++
#in all elif statment while calculating the the totalPrice there quantity is being multiplied by headPhone in every case
# change the PS5 to Ps5 because PS5 is not being analysed as a variable it is an keyword 
#added an else statment for adding the logic if an invalid name is entered

headPhone = int(999)
smartWatch = 1599
Ps5 = 1299
iPad = 599


productName = input("Enter Product Name: ")


quantity = int(input("Enter the Quantity of the Product: "))

totalPrice=1

if productName == "headPhone":
    totalPrice = (headPhone * quantity)

elif productName == "smartWatch":
    totalPrice = (smartWatch * quantity)

elif productName == "Ps5":
    totalPrice = (Ps5 * quantity)

elif productName == "iPad":
    totalPrice = (iPad * quantity)
else:
    print("InValid Product Name")


print ("Total Amount To Be Paid:" ,totalPrice)