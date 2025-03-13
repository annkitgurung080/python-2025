print("-------------Computer Bazar---------------")
print("1. Del(Rs.20000) 2. Toshiba(Rs.30000) 3.Mac(Rs.50000)")
dell_price=0
toshiba_price=0
mac_price=0
product_name=""
quantity=0

option=int(input("Enter the option: "))

if option==1:
    quantity = int(input("Enter the quantity: "))
    dell_price = 20000*quantity
    product_name = "Dell"
elif option==2:
    quantity = int(input("Enter the quantity: "))
    toshiba_price = 30000*quantity
    product_name = "Toshiba"
elif option==3:
    quantity = int(input("Enter the quantity: "))
    mac_price = 50000*quantity
    product_name = "Mac"
else:
    print("Invalid option !")
    exit()

delivery_charge=0
print("1.Home(Rs.1000) 2.Pickup(Rs.0)")
del_option=int(input("Enter the delivery option: "))
if del_option ==1:
    delivery_charge=1000

packing_charge=0
print("Packing: 1. Plastic Bag(Rs.1000) 2. Bag(Rs.2000) 3.Gift box(5000) 4.None")
pack_option = int(input("Enter the packaging option: "))
if pack_option ==1:
    packing_charge=1000
elif pack_option == 2:
    packing_charge=2000
elif pack_option == 3:
    packing_charge=5000


print("Location: 1.Kathmandu(Rs.13% tax) 2.Lalitur(Rs.0%tax) 3. Bhaktapur(Rs.0% tax)")
total=dell_price+toshiba_price+mac_price
location=int(input("Enter the location option:"))
tax_amount=0
if location ==1:
    tax_amount = total*0.13


grand_total = total+delivery_charge+packing_charge+tax_amount
print("----------Bill-----------")
print("Product Name: ",product_name)
print("Quantity: ",quantity)
print("Total: ",total)
print("Delivery Charge: ",delivery_charge)
print("Packing Charge: ",packing_charge)
print("Tax Amount: ",tax_amount)
print("Grand Total: ",grand_total)
print("Thankyou for shopping with us ")