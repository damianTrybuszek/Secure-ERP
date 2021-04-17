from model.crm import crm
from view import terminal as view
from model import data_manager as d_man
from model import util

ID_INDEX = 0
NAME_INDEX = 1
EMAIL_INDEX = 2
SUBSCRIPTION_INDEX = 3



def list_customers():

    lines = d_man.read_table_from_file(crm.DATAFILE, separator=';')
    
    view.print_table(lines, crm.HEADERS)


def add_customer():

    lines = d_man.read_table_from_file(crm.DATAFILE, separator=';')

    table = ["","","",""]

    table[ID_INDEX] = util.generate_id()

    is_looping = True

    while is_looping:

        [table[NAME_INDEX], table[EMAIL_INDEX], table[SUBSCRIPTION_INDEX]] = view.get_inputs("Please provide name, email and subscription status")

        if len(table[NAME_INDEX]) < 4 or "@" not in table[EMAIL_INDEX] or "." not in table[EMAIL_INDEX] or table[SUBSCRIPTION_INDEX] not in ["0","1"]:
            view.print_error_message("Please provide correct data!")
        else:
            is_looping = False

    lines.append(table)
    
    d_man.write_table_to_file(crm.DATAFILE, lines, separator=';')

 
def update_customer():
    lines = d_man.read_table_from_file(crm.DATAFILE, separator=';')
    table = ["","","",""]

    table[ID_INDEX] = view.get_input("Please input user ID")
    is_looping = True
    
    for element in lines:
        if element[ID_INDEX] == table[ID_INDEX]:
            while is_looping:
                [table[NAME_INDEX], table[EMAIL_INDEX], table[SUBSCRIPTION_INDEX]] = view.get_inputs("Please provide name, email and subscription status")
                if len(table[NAME_INDEX]) < 4 or "@" not in table[EMAIL_INDEX] or "." not in table[EMAIL_INDEX] or table[SUBSCRIPTION_INDEX] not in ["0","1"]:
                    view.print_error_message("Please provide correct data!")
                else:
                    is_looping = False

            element[NAME_INDEX] = table[NAME_INDEX]
            element[EMAIL_INDEX] = table[EMAIL_INDEX]
            element[SUBSCRIPTION_INDEX] = table[SUBSCRIPTION_INDEX]
            d_man.write_table_to_file(crm.DATAFILE, lines, separator=';')
    if is_looping:
        view.print_error_message("There is no such ID.")




def delete_customer():
    lines = d_man.read_table_from_file(crm.DATAFILE, separator=';')
    table = ['']

    table[ID_INDEX] = view.get_input("Please input user ID")
    is_looping =True

    for element in lines:
        if element[ID_INDEX] == table[ID_INDEX]:
            lines.remove(element)
            d_man.write_table_to_file(crm.DATAFILE, lines, separator=';')
            is_looping = False

    if is_looping:
        view.print_error_message("There is no such ID.")


def get_subscribed_emails():
    lines = d_man.read_table_from_file(crm.DATAFILE, separator=';')
    
    subscribed_emails_list = []

    for element in lines:
        if element[SUBSCRIPTION_INDEX] == "1":
            subscribed_emails_list.append(element[EMAIL_INDEX])
    
    if len(subscribed_emails_list) > 0:
        view.print_general_results(subscribed_emails_list, "Subscribed Emails:")
    else:
        view.print_error_message("There are no subscribed emails!")



def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
