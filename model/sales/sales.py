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


def new_transaction():
    transaction_list = []
    for i in range(len(HEADERS)):
        user_input = view.get_input(HEADERS[i])
        transaction_list.append(user_input)
    TRANSACTIONS.append(transaction_list)
    return TRANSACTIONS


def valid_input():
    user_input = view.get_input("Do you want to save changes? Yes or No?").upper()
    if user_input == "YES" or user_input == "Y" or user_input == "NO" or user_input == "N": 
        return user_input
    else:
        new_valid_input = valid_input()
        return new_valid_input