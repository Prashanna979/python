import getpass


def register():
    username=input("enter username").strip()

    if username in open("user.txt").read():
        print("user already exists")
        exit()

    password = getpass.getpass("enter password").strip()
    confirm_password= getpass.getpass("confirm password").strip()
    if password!=confirm_password:
        print("password mismatch")
        exit()

    handle=open("user.txt","a")
    handle.write(f"f,username: {username} password: {password} \n")
    handle.close()

    print("user registered successfully")

register()




#
# import csv
# data=csv.reader(open("student.csv"))
# print(list(data))


# xampp