#Wahid Dawari
total = 0
Local_tax = 1.095
print("Welcome to Self Checkout!")
print("Please Enter Item Prices Individually.")
print("When Done, Enter: 0")
#storing the prices
#Loop until customer enters 0 
price = float(input("Enter First Item price: $"))
while price != 0: 
  total = float(price + total)
  price = float( input("Enter Next Item Price: $"))
#Adding on Tax
tax = input("Is Sales Tax Applicable? (y/n): ").lower()
print("")
if tax == "y" :
  print("Your total is: $", format(total * Local_tax, ",.2f"), sep = "")
  print("")
  Cash = float(input("Enter in Money Provided by Customer: $"))
  print("")
  #if they pay less than the total:
  while Cash < round(total * Local_tax, 2): 
   print("You still need to pay: $", round(((total * Local_tax) - Cash),2), sep = "")
   print("")
   print("Your Total is: $", format(total * Local_tax, ",.2f"), sep = "")
   print("")
   Cash = float(input("Enter in Money Provided by Customer: $"))
  #If they pay more or equal
  final_total = round(total * Local_tax, 2)
  print("Your Change is: $", format(Cash - ((final_total)), ",.2f"), sep = "")
  print("")
  print("Thank You for Shopping Here!")
#What if there is no tax
else: 
  print("Your total is: $", format(total, ",.2f"), sep = "")
  print("")
  Cash = float(input("Enter in Money Provided by Customer: $"))
  print("")
  #if they pay less than the total:
  while Cash < total : 
   print("You still need to pay: $", format(((total) - Cash), ",.2f"), sep = "")
   print("")
   print("Your Total is: $", total, sep = "")
   print("")
   Cash = float(input("Enter in Money Provided by Customer: $"))
  #what if they pay more or the exact amount: 
  if Cash >= total:
    print("Your Change is: $",  format(Cash - (total ),",.2f"), sep = "")
    print("")
    print("Thank You for Shopping Here!")
 #wahid dawari's second hip hw
