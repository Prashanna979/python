# age=int(input("enter your age"))
#
# if age>=18 and age<=40:
#     print("you can join the party")
#     if age >= 18 and age <= 25:
#         print("you can only drink  coke")
#     elif age > 25 and age <= 30:
#         print("you can drink both beer ")
#     else:
#         print("you can drink whiskey")
# else:
#     print("you arent eligible to join the party")
#
# users=[
#     ['admin', 'admin01'],
#     ['ram', 'ram001'],
#     ['ram1', 'ram002']
#
# ]
# username=input("enter your username")
# password=input("enter your password")
#
# if users[0][0]==username and users[0][1]==password:
#     print("welcome",username)
# elif users[1][0]==username and users[1][1]==password:
#     print("welcome", username)
# elif users[2][0] == username and users[2][1] == password:
#     print("welcome", username)
# else:
#     print("wrong username or password")


print("1.Ntc to Ntc -> rs 2.5 per 10 min")
print("2.Ntc to Ncell -> rs 3.5 per 10 min")
print("3.Ncell to ntc -> rs 4.5 per 10 min")
print("4.Ncell to Ncell -> rs 100% per 10 min")
option=int(input("enter your choice"))

print("call duration")
print("0.1-10min,1.10-20 ,2.20-30 ,3.30-50,4.40-50 ,5.50-60,6.60-70 ,7.70-80 ,8.80-90 ,9.90-100")
call_duration=int(input("enter your call duration:"))

if option==1:
    if call_duration==0:
        print("you get 2.5rs bonus",2.5*2)
    elif call_duration==1:
        print("you get 5 rs bonus")
    elif call_duration==2:
        print("you get 7.5rs bonus")
    elif call_duration==3:
        print("you get 10rs bonus")
    elif call_duration==4:
        print("you get 12.5rs bonus")
    elif call_duration==5:
        print("you get 15rs bonus")
    elif call_duration==6:
        print("you get 17.5rs bonus")
    elif call_duration == 7:
        print("you get 20rs bonus")
    elif call_duration==8:
        print("you get 22.5rs bonus")
    elif call_duration == 9:
        print("you get 25rs bonus")
    else:
        print("invalid option")

elif option==2:
    if call_duration==0:
        print("you get 2.5rs bonus")
    elif call_duration==1:
        print("you get 7 rs bonus")
    elif call_duration==2:
        print("you get 10.5rs bonus")
    elif call_duration==3:
        print("you get 14rs bonus")
    elif call_duration==4:
        print("you get 17.5rs bonus")
    elif call_duration==5:
        print("you get 21rs bonus")
    elif call_duration==6:
        print("you get 24.5rs bonus")
    elif call_duration == 7:
        print("you get 28rs bonus")
    elif call_duration==8:
        print("you get 31.5rs bonus")
    elif call_duration == 9:
        print("you get 31.5rs bonus")
    else:
        print("invalid option")

elif option==3:
    if call_duration==0:
        print("you get 4.5rs bonus")
    elif call_duration==1:
        print("you get 9 rs bonus")
    elif call_duration==2:
        print("you get 13.5rs bonus")
    elif call_duration==3:
        print("you get 18rs bonus")
    elif call_duration==4:
        print("you get 22.5rs bonus")
    elif call_duration==5:
        print("you get 27rs bonus")
    elif call_duration==6:
        print("you get 31.5rs bonus")
    elif call_duration == 7:
        print("you get 36rs bonus")
    elif call_duration==8:
        print("you get 40.5rs bonus")
    elif call_duration==9:
        print("you get 45rs bonus")
    else:
        print("invalid option")

elif option==4:
    if call_duration==0:
        print("you get 10rs bonus")
    elif call_duration==1:
        print("you get 20 rs bonus")
    elif call_duration==2:
        print("you get 30rs bonus")
    elif call_duration==3:
        print("you get 40rs bonus")
    elif call_duration==4:
        print("you get 50rs bonus")
    elif call_duration==5:
        print("you get 60rs bonus")
    elif call_duration==6:
        print("you get 70rs bonus")
    elif call_duration == 7:
        print("you get 80rs bonus")
    elif call_duration==8:
        print("you get 90rs bonus")
    elif call_duration==9:
        print("you get 100rs bonus")
    else:
        print("invalid option")
else:
    print("invalid option")

print("1.student,2.adult,3.senior citizen")
age=int(input("enter your group"))
print("1.kalanki,2.balaju,3.maharajgunj,4. chabahil,5.koteshor,6.astdobato,7.balkhu")
start=int(input("select your starting location"))
print("1.kalanki,2.balaju,3.maharajgunj,4.chabahil,5.koteshor,6.satdobato,7.balkhu")
ride=int(input("enter your destination"))

if age==1:
    if start==1:
        if ride==2:
            print("your bus charge is",(15*1-((15*1)*0.1)))
        elif ride==3:
            print("your bus charge is",(15*2-((15*2)*0.1)))
        elif ride==4:
            print("your bus charge is ",(15*3-((15*3)*0.1)))
        elif ride==5:
            print("your bus charge is ",(15*4-((15*4)*0.1)))
        elif ride==6:
            print("your bus charge is ",(15*5-((15*5)*0.1)))
        elif ride==7:
            print("your bus charge is ",(15*6-((15*6)*0.1)))
        elif ride==1:
            print("your bus charge is ",(15*7-((15*7)*0.1)))
        else:
            print("invalid option")

    elif start==2:
        if ride == 2:
            print("your bus charge is", (15*1-(15 * 1) * 0.1))
        elif ride == 3:
            print("your bus charge is", (15*2-(14 * 2) * 0.1))
        elif ride == 4:
            print("your bus charge is ", (15*3-(14 * 3) * 0.1))
        elif ride == 5:
            print("your bus charge is ", (15*4-(14 * 4) * 0.1))
        elif ride == 6:
            print("your bus charge is ", (15*5-(14 * 5) * 0.1))
        elif ride == 7:
            print("your bus charge is ", (15*6-(14 * 6) * 0.1))
        elif ride == 1:
            print("your bus charge is ", (15*7-(14 * 7) * 0.1))

    elif start==3:
        if ride == 2:
            print("your bus charge is", (15*1-(15 * 1) * 0.1))
        elif ride == 3:
            print("your bus charge is", (15*2-(14 * 2) * 0.1))
        elif ride == 4:
            print("your bus charge is ", (15*3-(14 * 3) * 0.1))
        elif ride == 5:
            print("your bus charge is ", (15*4-(14 * 4) * 0.1))
        elif ride == 6:
            print("your bus charge is ", (15*5-(14 * 5) * 0.1))
        elif ride == 7:
            print("your bus charge is ", (15*6-(14 * 6) * 0.1))
        elif ride == 1:
            print("your bus charge is ", (15*7-(14 * 7) * 0.1))

    elif start==4:
        if ride == 2:
            print("your bus charge is", (15*1-(15 * 1) * 0.1))
        elif ride == 3:
            print("your bus charge is", (15*2-(14 * 2) * 0.1))
        elif ride == 4:
            print("your bus charge is ", (15*3-(14 * 3) * 0.1))
        elif ride == 5:
            print("your bus charge is ", (15*4-(14 * 4) * 0.1))
        elif ride == 6:
            print("your bus charge is ", (15*5-(14 * 5) * 0.1))
        elif ride == 7:
            print("your bus charge is ", (15*6-(14 * 6) * 0.1))
        elif ride == 1:
            print("your bus charge is ", (15*7-(14 * 7) * 0.1))

    elif start==5:
        if ride == 2:
            print("your bus charge is", (15*7-(15 * 2) * 0.1))
        elif ride == 3:
            print("your bus charge is", (15*7-(14 * 3) * 0.1))
        elif ride == 4:
            print("your bus charge is ", (15*7-(14 * 4) * 0.1))
        elif ride == 5:
            print("your bus charge is ", (15*7-(14 * 5) * 0.1))
        elif ride == 6:
            print("your bus charge is ", (15*7-(14 * 6) * 0.1))
        elif ride == 7:
            print("your bus charge is ", (15*7-(14 * 7) * 0.1))
        elif ride == 1:
            print("your bus charge is ", (15*7-(14 * 8) * 0.1))

    elif start==6:
        if ride == 2:
            print("your bus charge is", (15*7-(15 * 2) * 0.1))
        elif ride == 3:
            print("your bus charge is", (15*7-(14 * 3) * 0.1))
        elif ride == 4:
            print("your bus charge is ", (15*7-(14 * 4) * 0.1))
        elif ride == 5:
            print("your bus charge is ", (15*7-(14 * 5) * 0.1))
        elif ride == 6:
            print("your bus charge is ", (15*7-(14 * 6) * 0.1))
        elif ride == 7:
            print("your bus charge is ", (15*7-(14 * 7) * 0.1))
        elif ride == 1:
            print("your bus charge is ", (15*7-(14 * 8) * 0.1))

    elif start==7:
        if ride == 2:
            print("your bus charge is", (15*7-(15 * 2) * 0.1))
        elif ride == 3:
            print("your bus charge is", (15*7-(14 * 3) * 0.1))
        elif ride == 4:
            print("your bus charge is ", (15*7-(14 * 4) * 0.1))
        elif ride == 5:
            print("your bus charge is ", (15*7-(14 * 5) * 0.1))
        elif ride == 6:
            print("your bus charge is ", (15*7-(14 * 6) * 0.1))
        elif ride == 7:
            print("your bus charge is ", (15*7-(14 * 7) * 0.1))
        elif ride == 1:
            print("your bus charge is ", (15*7-(14 * 8) * 0.1))
    else:
        print("invalid option")

elif age==2:
    if start==1:
        if ride==2:
            print("your bus charge is",(15*2))
        elif ride==3:
            print("your bus charge is",(14*3))
        elif ride==4:
            print("your bus charge is ",(14*4))
        elif ride==5:
            print("your bus charge is ",(14*5))
        elif ride==6:
            print("your bus charge is ",(14*6))
        elif ride==7:
            print("your bus charge is ",(14*7))
        elif ride==1:
            print("your bus charge is ",(14*8))
        else:
            print("invalid option")

    elif start==2:
        if ride == 2:
            print("your bus charge is", (15 * 2) )
        elif ride == 3:
            print("your bus charge is", (14 * 3) )
        elif ride == 4:
            print("your bus charge is ", (14 * 4) )
        elif ride == 5:
            print("your bus charge is ", (14 * 5) )
        elif ride == 6:
            print("your bus charge is ", (14 * 6) )
        elif ride == 7:
            print("your bus charge is ", (14 * 7) )
        elif ride == 1:
            print("your bus charge is ", (14 * 8) )

    elif start==3:
        if ride == 2:
            print("your bus charge is", (15 * 2) )
        elif ride == 3:
            print("your bus charge is", (14 * 3) )
        elif ride == 4:
            print("your bus charge is ", (14 * 4) )
        elif ride == 5:
            print("your bus charge is ", (14 * 5) )
        elif ride == 6:
            print("your bus charge is ", (14 * 6) )
        elif ride == 7:
            print("your bus charge is ", (14 * 7) )
        elif ride == 1:
            print("your bus charge is ", (14 * 8) )

    elif start==4:
        if ride == 2:
            print("your bus charge is", (15 * 2) )
        elif ride == 3:
            print("your bus charge is", (14 * 3) )
        elif ride == 4:
            print("your bus charge is ", (14 * 4) )
        elif ride == 5:
            print("your bus charge is ", (14 * 5) )
        elif ride == 6:
            print("your bus charge is ", (14 * 6) )
        elif ride == 7:
            print("your bus charge is ", (14 * 7) )
        elif ride == 1:
            print("your bus charge is ", (14 * 8) )

    elif start==5:
        if ride == 2:
            print("your bus charge is", (15 * 2) )
        elif ride == 3:
            print("your bus charge is", (14 * 3) )
        elif ride == 4:
            print("your bus charge is ", (14 * 4) )
        elif ride == 5:
            print("your bus charge is ", (14 * 5) )
        elif ride == 6:
            print("your bus charge is ", (14 * 6) )
        elif ride == 7:
            print("your bus charge is ", (14 * 7) )
        elif ride == 1:
            print("your bus charge is ", (14 * 8) )

    elif start==6:
        if ride == 2:
            print("your bus charge is", (15 * 2) )
        elif ride == 3:
            print("your bus charge is", (14 * 3) )
        elif ride == 4:
            print("your bus charge is ", (14 * 4) )
        elif ride == 5:
            print("your bus charge is ", (14 * 5) )
        elif ride == 6:
            print("your bus charge is ", (14 * 6) )
        elif ride == 7:
            print("your bus charge is ", (14 * 7) )
        elif ride == 1:
            print("your bus charge is ", (14 * 8) )

    elif start==7:
        if ride == 2:
            print("your bus charge is", (15 * 2) )
        elif ride == 3:
            print("your bus charge is", (14 * 3) )
        elif ride == 4:
            print("your bus charge is ", (14 * 4) )
        elif ride == 5:
            print("your bus charge is ", (14 * 5) )
        elif ride == 6:
            print("your bus charge is ", (14 * 6) )
        elif ride == 7:
            print("your bus charge is ", (14 * 7) )
        elif ride == 1:
            print("your bus charge is ", (14 * 8) )
    else:
        print("invalid option")

elif age==3:
    if start==1:
        if ride==2:
            print("your bus charge is",(15*2)*0.4)
        elif ride==3:
            print("your bus charge is",(14*3)*0.4)
        elif ride==4:
            print("your bus charge is ",(14*4)*0.4)
        elif ride==5:
            print("your bus charge is ",(14*5)*0.4)
        elif ride==6:
            print("your bus charge is ",(14*6)*0.4)
        elif ride==7:
            print("your bus charge is ",(14*7)*0.4)
        elif ride==1:
            print("your bus charge is ",(14*8)*0.4)
        else:
            print("invalid option")

    elif start==2:
        if ride == 2:
            print("your bus charge is", (15 * 2) * 0.4)
        elif ride == 3:
            print("your bus charge is", (14 * 3) * 0.4)
        elif ride == 4:
            print("your bus charge is ", (14 * 4) * 0.4)
        elif ride == 5:
            print("your bus charge is ", (14 * 5) * 0.4)
        elif ride == 6:
            print("your bus charge is ", (14 * 6) * 0.4)
        elif ride == 7:
            print("your bus charge is ", (14 * 7) * 0.4)
        elif ride == 1:
            print("your bus charge is ", (14 * 8) * 0.4)

    elif start==3:
        if ride == 2:
            print("your bus charge is", (15 * 2) * 0.4)
        elif ride == 3:
            print("your bus charge is", (14 * 3) * 0.4)
        elif ride == 4:
            print("your bus charge is ", (14 * 4) * 0.4)
        elif ride == 5:
            print("your bus charge is ", (14 * 5) * 0.4)
        elif ride == 6:
            print("your bus charge is ", (14 * 6) * 0.4)
        elif ride == 7:
            print("your bus charge is ", (14 * 7) * 0.4)
        elif ride == 1:
            print("your bus charge is ", (14 * 8) * 0.4)

    elif start==4:
        if ride == 2:
            print("your bus charge is", (15 * 2) * 0.4)
        elif ride == 3:
            print("your bus charge is", (14 * 3) * 0.4)
        elif ride == 4:
            print("your bus charge is ", (14 * 4) * 0.4)
        elif ride == 5:
            print("your bus charge is ", (14 * 5) * 0.4)
        elif ride == 6:
            print("your bus charge is ", (14 * 6) * 0.4)
        elif ride == 7:
            print("your bus charge is ", (14 * 7) * 0.4)
        elif ride == 1:
            print("your bus charge is ", (14 * 8) * 0.4)

    elif start==5:
        if ride == 2:
            print("your bus charge is", (15 * 2) * 0.4)
        elif ride == 3:
            print("your bus charge is", (14 * 3) * 0.4)
        elif ride == 4:
            print("your bus charge is ", (14 * 4) * 0.4)
        elif ride == 5:
            print("your bus charge is ", (14 * 5) * 0.4)
        elif ride == 6:
            print("your bus charge is ", (14 * 6) * 0.4)
        elif ride == 7:
            print("your bus charge is ", (14 * 7) * 0.4)
        elif ride == 1:
            print("your bus charge is ", (14 * 8) * 0.4)

    elif start==6:
        if ride == 2:
            print("your bus charge is", (15 * 2) * 0.4)
        elif ride == 3:
            print("your bus charge is", (14 * 3) * 0.4)
        elif ride == 4:
            print("your bus charge is ", (14 * 4) * 0.4)
        elif ride == 5:
            print("your bus charge is ", (14 * 5) * 0.4)
        elif ride == 6:
            print("your bus charge is ", (14 * 6) * 0.4)
        elif ride == 7:
            print("your bus charge is ", (14 * 7) * 0.4)
        elif ride == 1:
            print("your bus charge is ", (14 * 8) * 0.4)

    elif start==7:
        if ride == 2:
            print("your bus charge is", (15 * 2) * 0.4)
        elif ride == 3:
            print("your bus charge is", (14 * 3) * 0.4)
        elif ride == 4:
            print("your bus charge is ", (14 * 4) * 0.4)
        elif ride == 5:
            print("your bus charge is ", (14 * 5) * 0.4)
        elif ride == 6:
            print("your bus charge is ", (14 * 6) * 0.4)
        elif ride == 7:
            print("your bus charge is ", (14 * 7) * 0.4)
        elif ride == 1:
            print("your bus charge is ", (14 * 8) * 0.4)
else:
    print("invalid option")