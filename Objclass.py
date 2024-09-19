class item():
    def __init__(self, name, cust, interest):
        self.__objName = name
        self.__cust = cust
        self.__interest =  interest


    def price(self):
        return self.__cust+((self.__interest/100)*self.__cust)
        

    def editItem(self, name=None,cust=None,interest=None):
        if name !=None:
            self.__objName = name
        if cust !=None:
            self.__cust=cust
        if interest!=None:
            self.__interest  = interest
    
    def printInfo(self):
        print(f'Name: {self.__objName}')
        print(f'Cust: {self.__cust}')
        print(f'Final price: R$ {self.price():.2f}')
        print(f'Interest: {self.__interest}')


a = item("merda", 100, 2)
a.printInfo()

a.editItem("", 300, 50)
a.printInfo()

menu={1:"", 2:"",3:""}
i = 1
while True:
    name=input("Give the name: ")
    cust=float(input("How much it cost: "))
    interest=float(input("interest: "))

    if name == "-1" or cust <= -1 or interest<=-1:
        print("nope")
        break
    else:
        menu[i] = item(name, cust, interest)
        menu[i].printInfo()
        i+=1

print(menu[1].printInfo)
        
