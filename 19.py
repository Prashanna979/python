# class laptop:
#     def brand(self,name,model):
#         print("the brand of laptop is :",name)
#         print("the model is :",model)

#     def price(self,price):
#         print("the price of laptop is:",price)

# class dell(laptop):
#     def quantity(self,quantity):
#         print("the quantity of laptop is ",quantity)

# class toshiba(laptop):
#     pass


# dobj=dell()
# tobj=toshiba()
# dobj.brand("dell",4156)
# dobj.price(20000)
# dobj.quantity(2)
# tobj.brand("toshiba","a23")
# tobj.price(20000)

class bank:
    __account=897456487465

    def getaccount(self):
        return self.__account
    
    def setaccount(self,__account):
        self.__account=__account

bobj=bank()
bobj.setaccount(16541651645)
print(bobj.getaccount())