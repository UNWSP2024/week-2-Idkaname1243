p1 = input("Enter the item you wish to purchase:    ")
i1 = int(input("enter the price of the item you wish to purchase:   $"))
p2 = input("Enter the item you wish to purchase:   ")
i2 = int(input("enter the price of the item you wish to purchase:   $"))
p3 = input("Enter the item you wish to purchase:   ")
i3 = int(input("enter the price of the item you wish to purchase:   $"))
p4 = input("Enter the item you wish to purchase:   ")
i4 = int(input("enter the price of the item you wish to purchase:   $"))
p5 = input("Enter the item you wish to purchase:   ")
i5 = int(input("enter the price of the item you wish to purchase:   $"))


subtotal = (i1 + i2 + i3 + i4 + i5)
sales_tax = (subtotal*0.07)
total_cost = (subtotal+sales_tax)
print("""



""")
def calculate_total_purchase():
    print("recipt")
    print("items purchased")
    print(p1+" $"+str(i1))
    print(p2+" $"+str(i2))
    print(p3+" $"+str(i3))
    print(p4+" $"+str(i4))
    print(p5+" $"+str(i5))
    print("your subtotal is $"+ str(subtotal))
    print("your sales tax is $"+ str(sales_tax))
    print("your total cost is $"+ str(total_cost))
calculate_total_purchase()
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    # then displays the subtotal of the sale,
    # the amount of sales tax, and the total.
    # Assume the sales tax is 7 percent.

