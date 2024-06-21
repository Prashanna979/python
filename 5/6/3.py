# # WHILE LOOP
#
# x=10
# while x>=1:
#     print(x)
#     x-=1

# data=['apple','banana','cherry','grape']
# i=0
# while i<len(data):
#     print(data[i])
#     i+=1

# no_student=int(input("enter the no of students"))

# x=1
#
# while x<=no_student:
#     print(f"======student id:{x}=====")
#     for a in range(1):
#         nep=int(input("enter nepali marks: "))
#         eng = int(input("enter english marks: "))
#         sci = int(input("enter science marks: "))
#         math = int(input("enter math marks: "))
#         comp = int(input("enter computer marks: "))
#         total=nep+eng+sci+math+comp
#         students_marks.append(total)
#
#     x+=1
#
# sid=1
# for total in students_marks:
#     per=total/5
#     grade=''
#     if per>35 and per<=45:
#         grade='C'
#     elif per>45 and per<=60:
#         grade='B'
#     elif per>60 and per<=75:
#         grade='A'
#     elif per>75 and per<=100:
#         grade='A+'
#     else:
#         grade='F'
#     print(f"id:{sid} Total marks: {total} percentage:{per} Grade:{grade}")
#     # print("id=",sid,"total= ",total,"per=",per, "grade=",grade)
#     sid+=1
#
# numbers=[12,13,14,15,12,13,14]
# num=[]
#
# for x in numbers:
#     if x not in num:
#         num.append(x)
# print(num)
#
# data=[12,34,65,56]
# data1=[25,45,67,78]
# numbers=[]
# i=0
#
# while i<len(data) and i<len(data1):
#     sum=[data[i]+data1[i]]
#     numbers.append(sum)
#     i+=1
# print("sum= ",numbers)

#
#
# users=[
#     {'id':1,'name':'ram','gender':'male','status':True},
#     {'id':2,'name':'sophia','gender':'female','status':False},
#     {'id':3,'name':'hari','gender':'male','status':False},
#     {'id':4,'name':'gopal','gender':'male','status':True},
#     {'id':5,'name':'rita','gender':'female','status':False},
#     {'id':6,'name':'laxmi','gender':'female','status':True},
#
# ]
#
# total_users=len(users)
# print("total no of users are:",total_users)
#
# total_male = sum(1
#     for user in users
#         if user['gender'] == 'male'
# )
# print("total no of males are:",total_male)
#
# total_female = sum(1
#     for user in users
#         if user['gender'] == 'male'
# )
# print("total no of females are:",total_female)
#
# active_count = sum(1 for user in users if user['status'])
# print("Total number of active users:", active_count)
#
# inactive_count = sum(1 for user in users if not user['status'])
# print("Total number of inactive users:", inactive_count)
#
# active_male_count = sum(1 for user in users if user['gender'] == 'male' and user['status'])
# print("Total number of active male users:", active_male_count)
#
# inactive_male_count = sum(1
#     for user in users
#         if user['gender'] == 'male' and not user['status'])
# print("Total number of inactive male users:", inactive_male_count)
#
# active_female_count = sum(1 for user in users if user['gender'] == 'female' and user['status'])
# print("Total number of active female users:", active_female_count)
#
# inactive_female_count = sum(1
#     for user in users
#         if user['gender'] == 'female' and not user['status'])
# print("Total number of inactive female users:", inactive_female_count)


# total_users=?
# total_male=?
# total_female=?
# total_active_user=?
# total_inactive_user=?
# total_active_male=?
# total_active_female=?
# total_inactive_male=?
# total_inactive_female=?


#
#
users=[
    {'username':"admin",'password':'admin'},
    {'username':"ram",'password':'ram'},
    {'username':"sita",'password':'sita'},
    {'username':"hari",'password':'hari'}
]

books=[
    {'id':1,'name':'python','price':1000},
    {'id':2,'name':'java','price':2000},
    {'id':3,'name':'c++','price':3000},
    {'id':4,'name':'c#','price':4000},
    {'id':5,'name':'php','price':5000},
    {'id':6,'name':'ruby','price':6000},
    {'id':7,'name':'perl','price':7000},
    {'id':8,'name':'javascript','price':8000},
    {'id':9,'name':'html','price':9000},
    {'id':10,'name':'css','price':10000},
]
username=input("enter your username")
password=input("enter your password")

is_login=False

for user in users:
    if user['username'] == username and user['password'] == password:
        is_login=True

if is_login:
    print(f"welcome",username)
    for book in books:
        print(f"book id:{book['id']} book name:{book['name']} book price:{book['price']}")
else:
    print("invalid username or password")

