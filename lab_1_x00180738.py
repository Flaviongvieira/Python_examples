# example stock take

menu_option = 0
stock = []

# function to determine the index in a 2d matrix
def index_2d(stock, v):
    for index, item in enumerate(stock):
        if v in item:
            return index, item.index(v)

while menu_option != 4:
    print("\t***********************")
    print("\t* Menu *")
    print("\t***********************")
    print("\t* 1) Add Stock *")
    print("\t* 2) Stock List *")
    print("\t* 3) Stock Sale *")
    print("\t***********************")
    print("\t* 4) Exit *")
    print("\t***********************")
    menu_option = int(input("\tPlease enter menu option:"))
    if menu_option == 1:
        list_id = [row[0] for row in stock]
        idd = input("enter an ID: \t")
        if idd in list_id:
            print('Stock already exists!')
            qty = int(input("please enter a qty: \t"))

            # find the idd index position
            idd_index = index_2d(stock, idd)

            # add the current qty and new qty (we know the column = 3)
            idd_index_row = idd_index[0]
            current_qty = stock[idd_index_row][3]
            # print(current_qty)
            new_qty = current_qty + qty
            # print(new_qty)
            stock[idd_index_row][3] = new_qty
            # print(stock[idd_index_row][3])

        else:
            desc = input("please enter a description: \t")
            price = float(input("please enter a price: \t"))
            qty = int(input("please enter a qty: \t"))

            new_stock_item = [idd, desc, price, qty]
            stock.append(new_stock_item)
            print('New stock added!')


    elif menu_option == 2:
        for stock_item in stock:
            for info in stock_item:
                print("{0:<15}".format(info), end="")
            print()
    elif menu_option == 3:
        list_id = [row[0] for row in stock]
        if not list_id:
            print('stock list is empty!')
        else:
            idd = input("enter an existing ID: \t")
            while idd not in list_id:
                print('Stock does not exist')
                idd = input("enter an existing ID: \t")
            else:
                qty = int(input("please enter a qty for sale: \t"))
                if qty < 0:
                    print('Negative qty not allowed!')
                else:
                    # find the idd index position
                    idd_index = index_2d(stock, idd)
                    # add the current qty and new qty (we know the column = 3)
                    idd_index_row = idd_index[0]
                    current_qty = stock[idd_index_row][3]
                    if current_qty < qty:
                        print('Not enough qty in stock for this sale!')
                    else:
                        # print(current_qty)
                        new_qty = current_qty - qty
                        # print(new_qty)
                        stock[idd_index_row][3] = new_qty
                        # print(stock[idd_index_row][3])

    elif menu_option == 4:
        pass
    else:
        print("Error - Please enter number between 1 and 4.")
