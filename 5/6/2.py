# FOR LOOP


# data=['apple','banana','cherry']
# for fruit in data:
#      if fruit== 'apple':
#          print(fruit)

# numbers=[34,11,13,54,67,99,88,78]
# total=0
# for number in numbers:
    # print("number is",number)
#     total+=1
#
# print(total)

# even=0
# odd=0
# total=0
# for i in range(1,25):
#
#     # print("welcome python class")
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
#     total+=i
# print("sum even",even)
# print("sum odd",odd)
# print("total",total)

# numbers=[
#     [25,15,35,45,66],
#     [44,66,99,7,88],
#     [11,44,77,88,99]
# ]
# for number in numbers:
#     for num in number:
#         # print(num,end=" ")
#         if num%2==0:
#             print(num,end=" ")

# st=[]
# num=int(input("enter the no of students"))
# for i in range(num):
#     name=input("enter students name")
#     st.append(name)
# print(st)

# for x in range(1,11):
#     for y in range(1,11):
#         print(f"{x}*{y} = {x*y}",end=" ,")
#         print()

#i am ram i live in ktm

# dic={'Id':1,'Name':"ram","address":"bkt"}
# print(dic["Name"])

students=[
    {'id': 1, "Name": "ram", "address": "ktm"},
    {'id':1, "Name": "hari","address":"ltp"},
    {'id':1, "Name": "gopal","address":"bkt"},
    {'id':1, "Name": "sophia","address":"bkt"},
    {'id':1, "Name": "laxmi","address":"ktm"}
]

for student in students:
       print("i am", student["Name"],"i live in",student["address"])