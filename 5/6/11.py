# name=input("enter your name")
# eng=int(input("enter your english marks"))
# sci=int(input("enter your science marks"))
# math=int(input("enter your math marks"))
# soc=int(input("enter your social marks"))
# nep=int(input("enter your nepali marks"))
# total=eng+sci+math+soc+nep
#
# per=total/5
# grade=''
# if per>35 and per<=45:
#     grade='C'
# elif per>45 and per<=60:
#     grade='B'
# elif per>60 and per<=75:
#     grade='A'
# elif per>75 and per<=100:
#     grade='A+'
# else:
#     grade='F'
#     print()
#
# handle=open("user.txt","a")
#
# handle.write(f"name:{name} Total marks: {total} percentage:{per} Grade:{grade}")
# handle.write("\n")
# handle.close()

# print("=========COMPUTER BAZAAR")
# name = input("enter your name ")
# phone = int(input("enter your phone number"))
#
# dell = 20000
# toshiba = 30000
# mac = 50000
#
# print("dell price",dell)
# print("toshiba price",toshiba)
# print("mac price",mac)
#
# number1 = int(input("enter how many dell laptops you want to buy: "))
# number2 = int(input("enter how many toshiba laptops you want to buy: "))
# number3 = int(input("enter how many mac laptops you want to buy: "))
# price = number1*dell+number2*toshiba+number3*mac
# print(price)
#
# print("1. Home delivery(rs 1000)")
# print("2. Pickup(Free)")
# option1 = int(input("choose your delivery option"))
# if option1 == 1:
#     deli = 1000
# else:
#     deli = 0
# print("your delivery charge is ", deli)
#
# print("1. plastic(rs 1000)")
# print("2. bag(rs 2000)")
# print("3. Gift box(rs 5000)")
# print("4. None")
# option2 = int(input("choose your packing choice"))
# if option2 == 1:
#     pack = 1000
# elif option2 == 2:
#     pack = 2000
# elif option2 == 3:
#     pack = 5000
# else:
#     pack = 0
#
#
# print("1. ktm")
# print("2. ltp")
# print("3. bkt")
# option = int(input("enter your location"))
#
# if option == 1:
#     print("13 percent tax")
#     tax = price*(13/100)
#
# else:
#     tax = 0
# # print("your tax charge is:", tax)
#
# grand_total = price+deli+pack+tax
# print("==BILL==")
#
# handle=open("bill.txt","w")
# handle.write(f"=====BILL====== \n name:{name}\n dell laptops:{number1}\n toshiba laptops:{number2}\n mac laptops:{number3}\n Delivery type:{deli}\n Packing type:{pack}\n   phone no.: {phone}\n tax: {tax} \n Grand Total: {grand_total}")
# handle.close()

#
data=open("user.txt","r")
# print(data.read())
print(data.readlines())