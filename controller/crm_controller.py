from model.crm import crm
from view import terminal as view
from model import data_manager as d_man
from model import util


def list_customers():

    lines = d_man.read_table_from_file(crm.DATAFILE, separator=';')
    
    view.print_table(lines, crm.HEADERS)


def add_customer():
    # table = [[tab1],[tab2],[tab3],[tab4]]

    id = util.generate_id()

    is_looping = True

    while is_looping:

        [name, email, subscript] = view.get_inputs("Please provide name, email and subscription status:  ")

        if len(name) < 4:
            raise NameError("Try to provide correct name\n")
        elif "@" not in email:
            raise NameError("Try to provide correct email\n")
        elif  subscript != "0" and subscript !="1":
            raise ValueError("Subscription status supposed to be 0 or 1.\n")
        is_looping = False

    table = [[id],[name],[email],[subscript]]
    
    d_man.write_table_to_file(crm.DATAFILE, table, separator=';')

 
def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


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
