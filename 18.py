# class calculator:
#     def add(self,x,y):
#         return x+y
    
#     def sub(self,x,y):
#         return x-y
    
#     def mul(self,x,y):
#         return x*y
    
#     def div(self,x,y):
#         return x/y
    
# obj=calculator()
# print(obj.add(2,3))
# print(obj.sub(8,3))
# print(obj.mul(2,3))
# print(obj.div(9,3))


# class products:
#     def add_products(self,name,price,quantity):
#         handle=open("user.txt","a")
#         handle.write(f"name:{name} price: {price} quantity:{quantity}")
#         handle.write("\n")
#         handle.close()

#     def show_products(self):
#         data=open("user.txt","r")
#         print(data.read())


# p=products()
# p.add_products("laptop",2000,2)
# p.show_products()





# inhertance
# setter and getter 
# scope of vairables
# construtor and destructor
# method overloading
# static method
# class method 
# property decorators

# constructor
class laptop:

    def __del__(self):
        print("i am batman")

    def __init__(self,name):
        self.name=name
        print("i am constructor")

    def __str__(self):
        print( f'The type is {self.name}')

obj=laptop("dell")
print(str(obj))

