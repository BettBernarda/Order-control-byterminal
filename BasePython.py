import math

menuDic = {}      
waitingDic = {}    
invoiceSum = 0 
dayMoneyDic = {} 
custSum = 0    
cashOpeningStatus = 0  
allTimeIncome=0
allTimeCust=0


def stylesSpace():
    print()
def returnToDashboard():
    global invoiceSum, custSum, menuDic, dayMoneyDic, dateCustDic, waitingDic
 
    return dashboard( menuDic, dayMoneyDic, waitingDic)

def returnToOrder():
    global invoiceSum, custSum, menuDic, dayMoneyDic, waitingDic

    return order(waitingDic, menuDic)

def returnToMenu():
    global menuDic, cashOpeningStatus
    return menu(menuDic, cashOpeningStatus)

def addOrderTicket(dataBaseMenu, waitingLine, clientId):
    print("/" * 20, 'Menu', "/" * 20)
    print("Digite -1 para voltar")
    print("-----------------")
    for key, value in dataBaseMenu.items():
        print(f"{key}. {value[0]} R${value[1]}")
        print("-----------------")
    while True:
        try:
            stylesSpace()
            choseItem = int(input("Adicionar: "))
            if choseItem == -1:
                break
            elif choseItem in dataBaseMenu:
                if clientId not in waitingLine:
                    waitingLine[clientId] = []
                waitingLine[clientId].append(dataBaseMenu[choseItem])
                stylesSpace()
                mentionMenu =dataBaseMenu[choseItem]
                print(mentionMenu[1], "adicionado com sucesso.")
                stylesSpace()
            else:
                stylesSpace()
                print("Item não encontrado, tente novamente.")
                stylesSpace()
        except ValueError:
            print("Entrada inválida, tente novamente.")
        continue

def delOrderTicket(clientId, waitingLine, dataBaseMenu):
    try:
        if not waitingLine[clientId]:
            input("Nenhum item no pedido, pressione enter para retornar")
            stylesSpace()
        else:
            print("-----------------")
            for i, item in enumerate(waitingLine[clientId], start=1):
                print(f"{i}. {item[0]} R${item[1]:.2f}")
                print("-----------------")
            stylesSpace()
            itemToDel = int(input("Qual item gostaria de deletar? "))
            if itemToDel == -1:
                return
            elif 0 < itemToDel <= len(waitingLine[clientId]):
                del waitingLine[clientId][itemToDel - 1]
                print("Item removido com sucesso.")
            else:
                print("Item não encontrado.")
    except ValueError:
        print("Entrada inválida, tente novamente.")

def ticketAnalysis(waitingLine, dataBaseMenu):
    stylesSpace()
    clientId = input("Nome de referência: ").upper()
    if clientId not in waitingLine:
        waitingLine[clientId] = []
        print("\n"*200)
    while True:
        print('/' * 20, f"Pedidos {clientId}", '/' * 20)
        stylesSpace()
        print("-----------------")
        if not waitingLine[clientId]:
            print("Nenhum item no pedido.")
            print("-----------------")
            stylesSpace
        else:
            for i, item in enumerate(waitingLine[clientId], start=1):
                print(f"{i}. {item[0]} R${item[1]:.2f}")
                print("-----------------")
                stylesSpace()
        orderOptions = input("[A] Adicionar [E] Excluir [V] Voltar       ").upper()[0]
        if orderOptions not in ["A", "E", "V"]:
            stylesSpace()
            input("Opção inválida, tente novamente! (Pressione enter para voltar)")
            stylesSpace()
        elif orderOptions == "A":
            stylesSpace()
            addOrderTicket(dataBaseMenu, waitingLine, clientId)
        elif orderOptions == "E":
            stylesSpace()
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
    stylesSpace()
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
    stylesSpace()
    print("-----------------")
    if not waitingLine:
        print("Ainda sem pedidos")
        print("-----------------")
    else:
        for i, key in enumerate(waitingLine, start=1):
            print(f"{i}. {key}")
            print("-----------------")
    while True:
        stylesSpace()
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
        stylesSpace()
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
                    dataBaseMenu.update({currentCount: (itemName,math.sqrt(itemValue**2), math.sqrt(itemCost**2))})
                    currentCount += 1
        except ValueError:
            print("Valor inválido, tente novamente!")

def menu(dataBaseMenu, CashGate):
    while True:
        print("\n"*200)
        print("/" * 20, "Menu", "/" * 20)
        print("Número-> Preço-> Custo")
        print("-----------------")
        if not dataBaseMenu:
            print("Menu vazio")
            print("-----------------")
        else:
            for key, values in dataBaseMenu.items():
                print(f"{key}. {values[0]} R${float(values[1]):.2f} - R${float(values[2]):.2f}")
                print("-----------------")
       
        if CashGate == 0:
            options = input("[A] Adicionar item [D] Deletar Item [S] Sair:       ").upper()[0]
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
        
def results(moneyDataBase):
     global allTimeCust,allTimeIncome
     while True:
        stylesSpace
        print("-----------------")
        if not moneyDataBase:
            print("Sem datas registradas.")
            print("-----------------")
            input("Precione enter parar retornar")
            print("\n"*200)
            returnToDashboard()
        else:
            for key,values in moneyDataBase.items():
                print(f"{key} - Entradas:R${values[0]} - Saidas:R${values[1]} - Lucro:R${values[0]-values[1]}")
                print("-----------------")
        stylesSpace()
        resultsOptions = str(input("[V] Voltar  [A] Apagar dados")).upper()[0]
        stylesSpace()
        if resultsOptions == "V":
            print("\n"*200)
            returnToDashboard()
        elif resultsOptions == "A":
            resultToDel = input("Insira a data que deseja deletar(dia/mês/ano):  ")
            try:
                if resultToDel in moneyDataBase:
                    safetyQuestion = input("Deseja deletar este dado? [S] sim [N] Não      ").upper()[0]
                    if safetyQuestion=="S":
                        resultToDelId=moneyDataBase[resultToDel]
                        allTimeCust-= resultToDelId[1]
                        allTimeIncome-= resultToDelId[0]
                        del moneyDataBase[resultToDel]

                    elif safetyQuestion=="N":
                        stylesSpace()
                        
                else:
                    stylesSpace()
                    input("data não encontrada, tente novamente! (Pressione enter para voltar)")
                    stylesSpace()
            except ValueError:
                stylesSpace()
                input("data não encontrada, tente novamente! (Pressione enter para voltar)")
                stylesSpace()




def dashboard(dataBaseMenu, moneyDataBase, waitingLine):
    global cashOpeningStatus ,invoiceSum,custSum,allTimeCust, allTimeIncome
    while True:
        print("/" * 35)
        if cashOpeningStatus == 0:
            print(8*(" "),"CAIXA FECHADO",8*(" "))
        else:
            print(8*(" "),"CAIXA ABERTO",8*(" "))
        print("/" * 35)
        stylesSpace()
        print("Bem-vindo(a) ao OnCommand")
        print("-----------------")
        print(f"Faturamento registrado: R${allTimeIncome:.2f}")
        print(f"Custo total registrado: R${allTimeCust:.2f}")
        print("-----------------")
        print(f"Faturamento do dia: R${invoiceSum:.2f}")
        print(f"Lucro do dia: R${invoiceSum-custSum:.2f}")
        print("-----------------")
        stylesSpace()
        if cashOpeningStatus == 0:
            while True:
                dashboardOptions = input("[M] Menu  [A] Abrir caixa  [R] Relatório     ").upper()[0]
                if dashboardOptions == "M":
                    return menu(dataBaseMenu, cashOpeningStatus)
                elif dashboardOptions == "A":
                    if not dataBaseMenu:
                        stylesSpace()
                        input("Não pode prosseguir sem itens no Menu, pressione enter para retornar")
                        print("\n"*100)
                        return returnToDashboard()
                    else:
                        cashOpeningStatus += 1
                        print("\n"*200)
                        return returnToDashboard()
                elif dashboardOptions =="R":
                   results(moneyDataBase)
        
                else:
                    print("Opção inválida, tente novamente.")
        elif cashOpeningStatus == 1:
            while True:
                dashboardOptions = input("[M] Menu [P] Pedidos [F] Fechar Caixa       ").upper()[0]
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
                        moneyDataBase.update({f"{day}/{month}/{year}":[invoiceSum,custSum]})
                        allTimeIncome+=invoiceSum
                        allTimeCust+=custSum
                        invoiceSum=0
                        custSum=0
                        cashOpeningStatus = 0
                        print("\n"*200)
                        return invoiceSum,custSum, allTimeCust, allTimeIncome, returnToDashboard()
                else:
                    stylesSpace()
                    input("Opção inválida, tente novamente! (Pressione enter para voltar)")
                    stylesSpace()

dashboard( menuDic, dayMoneyDic,waitingDic) 