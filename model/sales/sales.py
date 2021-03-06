""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util
from view import terminal as view

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

ID_INDEX = 0
CUSTOMER_INDEX = 1
PRODUCT_INDEX = 2
PRICE_INDEX = 3
DATE_INDEX = 4
TRANSACTIONS = data_manager.read_table_from_file(DATAFILE, separator=';')


def list_of_transactions():
    return TRANSACTIONS


def add_new_transaction():
    transaction_list = []
    for i in range(len(HEADERS)):
        user_input = view.get_input("Please enter a " + "'" + HEADERS[i] + "'" + " of transaction: ")
        transaction_list.append(user_input)
    TRANSACTIONS.append(transaction_list)
    return TRANSACTIONS


def valid_input(list_of_transactions):
    user_input = view.get_input("Do you want to save changes? Yes or No?").upper()
    if user_input == "YES" or user_input == "Y":
        data_manager.write_table_to_file(DATAFILE, list_of_transactions, separator=';')
    elif user_input == "NO" or user_input == "N":
        return user_input
    else:
        new_valid_input = valid_input(list_of_transactions)
        return new_valid_input


def update_list():
    user_input_id = view.get_input("Please enter a " + "'" + HEADERS[ID_INDEX] + "'" + " of transaction: ")
    counter = 0
    for transaction in range(len(TRANSACTIONS)):  
        if user_input_id == TRANSACTIONS[transaction][ID_INDEX]:
            for i in range(len(HEADERS) - 1):
                user_input_update = view.get_input(HEADERS[i + 1])
                TRANSACTIONS[transaction][i + 1] = user_input_update
                counter += 1
        else:
            counter = 0
    return TRANSACTIONS, counter


def delete_list_element():
    user_input_id = view.get_input("Please enter a " + "'" + HEADERS[ID_INDEX] + "'" + " of transaction: ")
    counter = 0
    for transaction in range(len(TRANSACTIONS)):
        if user_input_id == TRANSACTIONS[transaction][ID_INDEX]:
            TRANSACTIONS.pop(transaction)
            counter += 1
        else:
            counter = 0
    return TRANSACTIONS, counter


def update_and_delete_transaction(list_of_transactions, counter):
    if counter == 0:
        view.print_message("There is no such transaction with this 'Id'")
    else:
        valid_input(list_of_transactions)
