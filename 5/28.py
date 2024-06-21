# x=18
# y=19
# z=15
#
# if x>y:
#     if x>z:
#         print("x is greater than y and z")
#     else:
#         print("z  is greater than x and y")
# else:
#     if y>z:
#         print("y is greater than x and z")
#     else:
#         print("z is greater than x and y")

# username='admin'
# password='admin2'
#
# if username=='admin':
#     if password=='admin2':
#         print("login success")
#     else:
#         print("wrong password")
# else:
#     print("wrong username")

# print("===========ATM============")
# pin=int(input("enter your pin"))
#
# if pin==0000:
#     my_amount=10000
#     print("1.Withdraw")
#     print("2.Check balance")
#     option = int(input("enter your choice"))
#     if option==1:
#         amount=int(input("enter the amount to withdraw"))
#         if amount>my_amount:
#             print("insufficient balance")
#         else:
#             new_balance=my_amount-amount
#             print("withdraw successful")
#             print("withdraw amount=",amount)
#             print("remaining balance=",new_balance)
#     elif option==2:
#         print("your balance is:",my_amount)
#     else:
#         print("invalid option")
# else:
#     print("invalid pin")

print("=========COMPUTER BAZAAR")
name = input("enter your name ")
phone = int(input("enter your phone number"))

dell = 20000
toshiba = 30000
mac = 50000

print("dell price",dell)
print("toshiba price",toshiba)
print("mac price",mac)

number1 = int(input("enter how many dell laptops you want to buy: "))
number2 = int(input("enter how many toshiba laptops you want to buy: "))
number3 = int(input("enter how many mac laptops you want to buy: "))
price = number1*dell+number2*toshiba+number3*mac
print(price)

print("1. Home delivery(rs 1000)")
print("2. Pickup(Free)")
option1 = int(input("choose your delivery option"))
if option1 == 1:
    deli = 1000
else:
    deli = 0
print("your delivery charge is ", deli)

print("1. plastic(rs 1000)")
print("2. bag(rs 2000)")
print("3. Gift box(rs 5000)")
print("4. None")
option2 = int(input("choose your packing choice"))
if option2 == 1:
    pack = 1000
elif option2 == 2:
    pack = 2000
elif option2 == 3:
    pack = 5000
else:
    pack = 0
print("your packing charge is", pack)

print("1. ktm")
print("2. ltp")
print("3. bkt")
option = int(input("enter your location"))

if option == 1:
    print("13 percent tax")
    tax = price*(13/100)

else:
    tax = 0
print("your tax charge is:", tax)

grand_total = price+deli+pack+tax
print("==BILL==")
print("Name:", name)
print("phone no.: ",phone)

print("your grand total price is: ", grand_total)
