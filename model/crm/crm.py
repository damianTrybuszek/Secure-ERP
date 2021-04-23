""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

ID_INDEX = 0
NAME_INDEX = 1
EMAIL_INDEX = 2
SUBSCRIPTION_INDEX = 3


CUSTOMERS = data_manager.read_table_from_file(DATAFILE, separator=';')

def list_the_customers():
    return data_manager.read_table_from_file(DATAFILE, separator=';')

def add_customers():
    data_manager.write_table_to_file(DATAFILE, CUSTOMERS, separator=';')

def create_customer(table):
    table[ID_INDEX] = util.generate_id()
    CUSTOMERS.append(table)
    add_customers()

def is_id_in_base(id):
    for element in CUSTOMERS:
        if element[ID_INDEX] == id:
            return True
    return False

def update_customers(id, table):
    for element in CUSTOMERS:
        if element[ID_INDEX] == id:
            element[NAME_INDEX] = table[NAME_INDEX]
            element[EMAIL_INDEX] = table[EMAIL_INDEX]
            element[SUBSCRIPTION_INDEX] = table[SUBSCRIPTION_INDEX]
            add_customers()
            return ("Customer updated")

def delete_customer(id):
    for element in CUSTOMERS:
        if element[ID_INDEX] == id:
            CUSTOMERS.remove(element)
            add_customers()
            return ("Customer deleted")
    return ("There is no ID in the base")

def get_emails_of_subscribent():
    subscribed_emails_list = []

    for element in CUSTOMERS:
        if element[SUBSCRIPTION_INDEX] == "1":
            subscribed_emails_list.append(element[EMAIL_INDEX])
    
    return subscribed_emails_list








