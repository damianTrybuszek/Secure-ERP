from model.sales import sales
from view import terminal as view
from model import data_manager as file_handling

ID_INDEX = 0
CUSTOMER_INDEX = 1
PRODUCT_INDEX = 2
PRICE_INDEX = 3
DATE_INDEX = 4
months = dict({"01": 1, "02": 2, "03": 3, "04": 4, "05": 5, "06": 6, "07": 7, "08": 8, "09": 9, "10": 10, "11": 11, "12": 12})
days = dict({"01": 1, "02": 2, "03": 3, "04": 4, "05": 5, "06": 6, "07": 7, "08": 8, "09": 9, "10": 10,
             "11": 11, "12": 12, "13": 13, "14": 14, "15": 15, "16": 16, "17": 17, "18": 18, "19": 19, "20": 20,
             "21": 21, "22": 22, "23": 23, "24": 24, "25": 25, "26": 26, "27": 27, "28": 28, "29": 29, "30": 30, "31": 31})


def list_transactions():
    list_of_transactions = sales.list_of_transactions()
    view.print_table(list_of_transactions, sales.HEADERS)





def add_transaction():
    list_of_transactions = sales.add_new_transaction()
    sales.valid_input(list_of_transactions)   


def update_transaction():
    update_list = sales.update_list()
    list_of_transactions = update_list[0]
    counter = update_list[1]
    sales.update_and_delete_transaction(list_of_transactions, counter)


def delete_transaction():
    update_list = sales.delete_list_element()
    list_of_transactions = update_list[0]
    counter = update_list[1]
    sales.update_and_delete_transaction(list_of_transactions, counter)


def biggest_revenue_product_and_transaction():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    try:
        biggest_revenue_transaction = float(lines[ID_INDEX][PRICE_INDEX])
        for line in range(len(lines)):
            if biggest_revenue_transaction < float(lines[line + 1][PRICE_INDEX]):
                biggest_revenue_transaction = float(lines[line + 1][PRICE_INDEX])
    except IndexError:
        for line in range(len(lines)):
            if biggest_revenue_transaction == float(lines[line][PRICE_INDEX]):
                return line
                    

def get_biggest_revenue_transaction():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    biggest_revenue_transaction_list = []
    line_of_biggest_revenue_transaction = biggest_revenue_product_and_transaction()
    biggest_revenue_transaction_list.append(lines[line_of_biggest_revenue_transaction])
    view.print_table(biggest_revenue_transaction_list, sales.HEADERS)


def get_biggest_revenue_product():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    line_of_biggest_revenue_product = biggest_revenue_product_and_transaction()
    view.print_message("The biggest revenue product is " + f"'{lines[line_of_biggest_revenue_product][PRODUCT_INDEX]}'")


def count_and_sum_transactions():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    user_input_start_date = view.get_input(sales.HEADERS[DATE_INDEX])
    user_input_end_date = view.get_input(sales.HEADERS[DATE_INDEX])
    user_range_date_list = [user_input_start_date, user_input_end_date]
    counter = 0
    sum_of_transactions = 0
    
    for line in range(len(lines)):
        transaction_date = lines[line][DATE_INDEX]
        month_of_user_input_start_date = months.get(user_range_date_list[0][5:7])
        month_of_user_input_end_date = months.get(user_range_date_list[1][5:7])
        month_of_transaction = months.get(transaction_date[5:7])
        day_of_user_input_start_date = days.get(user_range_date_list[0][8:10])
        day_of_user_input_end_date  = days.get(user_range_date_list[1][8:10])
        day_of_transaction = days.get(transaction_date[8:10])
        
        if transaction_date[0:4] > user_range_date_list[0][0:4] and transaction_date[0:4] < user_range_date_list[1][0:4]:
            counter += 1
            sum_of_transactions = float(sum_of_transactions) + float(lines[line][PRICE_INDEX])
        elif transaction_date[0:4] == user_range_date_list[0][0:4] or transaction_date[0:4] == user_range_date_list[1][0:4]:
            if transaction_date[0:4] == user_range_date_list[0][0:4]:
                if month_of_transaction >= month_of_user_input_start_date:
                    if month_of_transaction > month_of_user_input_start_date:
                        counter += 1
                        sum_of_transactions = float(sum_of_transactions) + float(lines[line][PRICE_INDEX])
                    else:
                        if day_of_transaction >= day_of_user_input_start_date:
                            counter += 1
                            sum_of_transactions = float(sum_of_transactions) + float(lines[line][PRICE_INDEX])
            elif transaction_date[0:4] == user_range_date_list[1][0:4]:
                if month_of_transaction <= month_of_user_input_end_date:
                    if month_of_transaction < month_of_user_input_end_date:
                        counter += 1
                        sum_of_transactions = float(sum_of_transactions) + float(lines[line][PRICE_INDEX])
                    else:
                        if day_of_transaction <= day_of_user_input_end_date:
                            counter += 1
                            sum_of_transactions = float(sum_of_transactions) + float(lines[line][PRICE_INDEX])
    return counter, sum_of_transactions


def count_transactions_between():
    transactions_operation = count_and_sum_transactions()
    counter = transactions_operation[0]
    view.print_message(f"The number of transactions carried out during the specified time period: {counter}")


def sum_transactions_between(): 
    transactions_operation = count_and_sum_transactions()
    sum_of_transactions = transactions_operation[1]
    view.print_message(f"The sum of transactions carried out during the specified time period: {sum_of_transactions}" + " $")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
