from model.sales import sales
from view import terminal as view
from model import data_manager as file_handling

ID_INDEX = 0
CUSTOMER_INDEX = 1
PRODUCT_INDEX = 2
PRICE_INDEX = 3
DATE_INDEX = 4


def list_transactions():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    view.print_table(lines, sales.HEADERS)


def add_transaction():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    add_transaction_list = []
    for i in range(len(sales.HEADERS)):
        user_input = view.get_input(sales.HEADERS[i])
        add_transaction_list.append(user_input)
    lines.append(add_transaction_list)
    file_handling.write_table_to_file(sales.DATAFILE, lines, separator=';')
    

def update_transaction():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    user_input_id = view.get_input(sales.HEADERS[0])
    for line in range(len(lines)):
        if user_input_id == lines[line][0]:
            for i in range(len(sales.HEADERS) - 1):
                user_input_update = view.get_input(sales.HEADERS[i + 1])
                lines[line][i + 1] = user_input_update
    if user_input_id != lines[line][0]:
        view.print_message("There is no such transaction with this Id")
    file_handling.write_table_to_file(sales.DATAFILE, lines, separator=';')


def delete_transaction():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    user_input_id = view.get_input(sales.HEADERS[0])
    for line in range(len(lines)):
        if user_input_id == lines[line][0]:
            lines.pop(line)
            return file_handling.write_table_to_file(sales.DATAFILE, lines, separator=';')
    if user_input_id != lines[line][0]:
        view.print_message("There is no such transaction with this Id")


def get_biggest_revenue_transaction():
    lines = file_handling.read_table_from_file(sales.DATAFILE, separator=';')
    try:
        for line in range(len(lines)):
            if float(lines[line][PRICE_INDEX]) < float(lines[line + 1][PRICE_INDEX]):
                biggest_revenue_transaction = float(lines[line + 1][PRICE_INDEX])
    except IndexError:
        for line in range(len(lines)):
            if biggest_revenue_transaction == float(lines[line][PRICE_INDEX]):
                biggest_revenue_transaction_list = []
                biggest_revenue_transaction_list.append(lines[line])
                view.print_table(biggest_revenue_transaction_list, sales.HEADERS)







def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


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
