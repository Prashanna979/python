#x=400
#y=400

#if x>y:
   # print("x is greater than y")
#elif x==y:
 #   print("they are equal")
#else:
 #   print("y is greater than x")

#age=20

#if age>=18:
  #  print("eligible to vote")
#else:
  #  print("not eligible to vote")

# x=4
# y=13
# z=14
# if x>y and x>z:
#     print("x is greater ")
# elif y>x and y>z:
#     print("y is greater")
# elif x==y and y==z:
#     print("they are equal")
# else:
#     print("z is greater")

# nep = int(input("enter nepali marks"))
# eng = int(input("enter english marks"))
# sci = int(input("enter science marks"))
#
# total=nep+eng+sci
# per = total/3
#
# if per>90:
#     print("grade A")
# elif per>70 and per<90:
#     print("grade B")
# elif per>50 and per <70:
#     print("grade C")
# else:
#     print("fail")

#wap to check whether a number is even or odd
#wap to enter any number and check whether it is divisible by 3 and 5
#wap to enter year and check whether it is leap year or not

# x=int(input("enter any number"))
# if x%2==0:
#     print("it is even")
# else:
#     print("it is odd")

# x=int(input("enter any number"))
# if x%3==0 and x%5==0:
#     print("it is divisible by both 3 and 5")
# elif x%3==0 and x%5!=0:
#     print("it is divisible by 3 only")
# elif x%3!=0 and x%5==0:
#     print("it is divisible by 5 only")
# else:
#     print("it isnt divisible by 3 or 5")

y=int(input("enter any year"))
if y%4==0 or y%100==0:
    print("it is a leap year ")
else:
    print("it is not a leap year")