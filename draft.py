#Wahid Dawari
print("Welcome to Self Checkout!") 
print("Please Enter Item Prices Individually")
print("When Done, Enter 0")
item_1 = float(input("Enter Price of Item 1: "))
if item_1 == 0:
 print("Your total is: 0")
elif item_1 > 0: 
   item_2 = float(input("Enter Next Price: "))
   if (item_2) == 0.00: 
    tax_2 = input("Is sales tax appilcable? ").lower()
    if tax_2 == "y": 
      total_1 = (item_1 * 1.095)
      print("Your total is: ", total_1 )
    else: 
      total = item_1 
      print("Your total is: ", total )
