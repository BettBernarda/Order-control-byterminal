menuDic = {}      
waitingDic = {}  
invoiceSum = 0 
dateIncomeDic = {}
custSum = 0   
dateCustDic = {}
cashOpeningStatus = 0  

def returnToDashboard():
    global invoiceSum, custSum, menuDic, dateIncomeDic, dateCustDic, waitingDic
 
    return dashboard( menuDic, dateIncomeDic, dateCustDic, waitingDic)

def returnToOrder():
    global invoiceSum, custSum, menuDic, dateIncomeDic, dateCustDic, waitingDic

    return order(waitingDic, menuDic)

def returnToMenu():
    global menuDic, cashOpeningStatus
    return menu(menuDic, cashOpeningStatus)

def addOrderTicket(dataBaseMenu, waitingLine, clientId):
    print("/" * 20, 'Menu', "/" * 20)
    print("Digite -1 para voltar")
    for key, value in dataBaseMenu.items():
        print(f"[{key}] {value[0]} R${value[1]}")
    while True:
        try:
            choseItem = int(input("Adicionar: "))
            if choseItem == -1:
                break
            elif choseItem in dataBaseMenu:
                if clientId not in waitingLine:
                    waitingLine[clientId] = []
                waitingLine[clientId].append(dataBaseMenu[choseItem])
                print(dataBaseMenu[choseItem][0], "adicionado com sucesso.")
                print()
            else:
                print("Item não encontrado, tente novamente.")
        except ValueError:
            print("Entrada inválida, tente novamente.")
        continue

def delOrderTicket(clientId, waitingLine, dataBaseMenu):
    try:
        if clientId in waitingLine and waitingLine[clientId]:
            for i, item in enumerate(waitingLine[clientId], start=1):
                print(f"{i}. {item[0]} R${item[1]:.2f}")
            itemToDel = int(input("Qual item gostaria de deletar? "))
            if itemToDel == -1:
                return
            elif 0 < itemToDel <= len(waitingLine[clientId]):
                del waitingLine[clientId][itemToDel - 1]
                print("Item removido com sucesso.")
            else:
                print("Item não encontrado.")
        else:
            print("Nenhum item no pedido.")
    except ValueError:
        print("Entrada inválida, tente novamente.")

def ticketAnalysis(waitingLine, dataBaseMenu):
    print()
    clientId = input("Nome de referência: ").upper()
    if clientId not in waitingLine:
        waitingLine[clientId] = []
        print("\n"*200)
    while True:
        print('/' * 20, f"Pedidos {clientId}", '/' * 20)
        if clientId in waitingLine and waitingLine[clientId]:
            for i, item in enumerate(waitingLine[clientId], start=1):
                print(f"{i}. {item[0]} R${item[1]:.2f}")
        else:
            print("Nenhum item no pedido.")
        orderOptions = input("[A] Adicionar [E] Excluir [V] Voltar       ").upper()[0]
        if orderOptions not in ["A", "E", "V"]:
            print()
            input("Opção inválida, tente novamente! (Pressione enter para voltar)")
            print()
        elif orderOptions == "A":
            addOrderTicket(dataBaseMenu, waitingLine, clientId)
        elif orderOptions == "E":
            delOrderTicket(clientId, waitingLine, dataBaseMenu)
        elif orderOptions == "V":
            print("\n"*200)
            return returnToOrder()


def sum_close_order(waitingLine, orderToClose):
    global invoiceSum,custSum
    for item in waitingLine[orderToClose]:
        invoiceSum+=item[1]
        custSum+=item[2]
    del waitingLine[orderToClose]
    print()
    print("Comanda Fechada com sucesso")
    print("\n"*200)
    return invoiceSum,custSum, returnToOrder()


def close_order(waitingLine):
    while True:
        orderToClose = input("Comanda a fechar (Nome cliente): ").upper()
        if orderToClose == "-1":
            return returnToOrder()
        elif orderToClose not in waitingLine:
            print("Comanda não encontrada, tente novamente!")
        else:
            sum_close_order(waitingLine, orderToClose)
            

def order(waitingLine, dataBaseMenu):
    print("/"*20,"Pedidos","/"*20)
    print()
    for i, key in enumerate(waitingLine, start=1):
        print(f"{i}. {key}")
    while True:
        orderOptions = input("[A] Editar/Adicionar  [F] Fechar pedido [V] Voltar ").upper()[0]
        if orderOptions == "A":
            ticketAnalysis(waitingLine, dataBaseMenu)
        elif orderOptions == "F":
            close_order(waitingLine)
        elif orderOptions == "V":
            print("\n"*200)
            return returnToDashboard()
        else:
            print("Opção inválida, tente novamente.")

def del_Menu(dataBaseMenu):
    while True:
        print("/" * 20, "Excluir item", "/" * 20)
        print("Digite -1 para voltar")
        for key, values in dataBaseMenu.items():
            print(f"{key}. {values[0]} R${float(values[1]):.2f}")
        try:
            deleteId = int(input("Deletar item (número): "))
            if deleteId == -1:
                return returnToMenu()
            elif deleteId not in dataBaseMenu:
                print("Item não encontrado.")
            else:
                dataBaseMenu.pop(deleteId)
                temporaryDic = {}
                currentCount = 1
                for key, values in dataBaseMenu.items():
                    temporaryDic.update({currentCount: values})
                    currentCount += 1
                dataBaseMenu.clear()
                dataBaseMenu.update(temporaryDic)
                print("Item excluído com sucesso.")
        except ValueError:
            print("Entrada inválida, tente novamente.")

def add_menu(dataBaseMenu):
    while True:
        print("/" * 20, "Novo item", "/" * 20)
        print('Digite "-1" para voltar ao menu')
        currentCount = len(dataBaseMenu) + 1
        itemName = input("Nome: ")
        if itemName == "-1":
            return returnToMenu()
        try:
            itemValue = float(input("Valor: "))
            if itemValue == -1:
                return menu(dataBaseMenu)
            elif itemValue <= 0:
                print("Valor inválido, tente novamente!")
            else:
                itemCost = float(input("Custo de produção: "))
                if itemCost == -1:
                    return menu(dataBaseMenu)
                else:
                    dataBaseMenu.update({currentCount: (itemName, itemValue, itemCost)})
                    currentCount += 1
        except ValueError:
            print("Valor inválido, tente novamente!")

def menu(dataBaseMenu, CashGate):
    while True:
        print("\n"*200)
        print("/" * 20, "Menu", "/" * 20)
        for key, values in dataBaseMenu.items():
            print(f"{key}. {values[0]} R${float(values[1]):.2f} - R${float(values[2]):.2f}")
        if CashGate == 0:
            options = input("[A] Adicionar item [D] Deletar Item [S] Sair: ").upper()[0]
            if options == "A":
                add_menu(dataBaseMenu)
            elif options == "D":
                del_Menu(dataBaseMenu)
            elif options == "S":
                print("\n"*200)
                return returnToDashboard()
        elif CashGate == 1:
            options = input("Pressione enter para retornar: ")
            print("\n"*200)
            return returnToDashboard()
allTimeIncome=0
allTimeCust=0
def dashboard(dataBaseMenu, dataBaseInvoice, dataBaseCust, waitingLine):
    global cashOpeningStatus ,invoiceSum,custSum,allTimeCust, allTimeIncome
    while True:
        print("/" * 40)
        print("Bem-vindo(a) ao OnCommand")
        print(f"Faturamento registrado: R${allTimeIncome:.2f}")
        print(f"Custo total registrado: R${allTimeCust:.2f}")
        print("-----------------")
        print(f"Faturamento do dia: R${invoiceSum:.2f}")
        print(f"Lucro do dia: R${invoiceSum-custSum:.2f}")
        print("-----------------")
        if cashOpeningStatus == 0:
            while True:
                dashboardOptions = input("[M] Menu  [A] Abrir caixa ").upper()[0]
                if dashboardOptions == "M":
                    return menu(dataBaseMenu, cashOpeningStatus)
                elif dashboardOptions == "A":
                    cashOpeningStatus += 1
                    print("\n"*200)
                    print("CAIXAR ABERTO")
                    return returnToDashboard()
                else:
                    print("Opção inválida, tente novamente.")
        elif cashOpeningStatus == 1:
            while True:
                dashboardOptions = input("[M] Menu [P] Pedidos [F] Fechar Caixa ").upper()
                if dashboardOptions == "M":
                    print("\n"*200)
                    return menu(dataBaseMenu, cashOpeningStatus)
                elif dashboardOptions == "P":
                    print("\n"*200)
                    return order(waitingLine, dataBaseMenu)
                elif dashboardOptions == "F":
                    while True:
                        day = int(input("Insira o dia de hoje: "))
                        if day == -1:
                            break
                        elif 0 > day or day > 31:
                            print("Valor incorreto, tente novamente.")
                            continue
                        month = int(input("Insira o mês: "))
                        if month == -1:
                            break
                        elif 0 > month or month > 12:
                            print("Valor incorreto, tente novamente.")
                            continue
                        year = int(input("Insira o ano: "))
                        if year == -1:
                            break
                        elif 0 > year or year > 9999:
                            print("Valor incorreto, tente novamente.")
                            continue
                        dataBaseInvoice.update({f"{day}/{month}/{year}":invoiceSum})
                        dataBaseCust.update({f"{day}/{month}/{year}":custSum})
                        allTimeIncome+=invoiceSum
                        allTimeCust+=custSum
                        invoiceSum=0
                        custSum=0
                        cashOpeningStatus = 0
                        print("\n"*200)
                        print("CAIXA FECHADO")
                        return invoiceSum,custSum, allTimeCust, allTimeIncome, returnToDashboard()

dashboard( menuDic, dateIncomeDic, dateCustDic,waitingDic)
