from model.crm import crm
from view import terminal as view

ID_INDEX = 0
NAME_INDEX = 1
EMAIL_INDEX = 2
SUBSCRIPTION_INDEX = 3

def list_customers():
    customers_list = crm.list_the_customers()
    view.print_table(customers_list, crm.HEADERS)

def add_customer():
    table = crm.TABLE

    [table[NAME_INDEX], table[EMAIL_INDEX], table[SUBSCRIPTION_INDEX]] = view.get_inputs("Please provide name, email and subscription status")

    if len(table[NAME_INDEX]) < 4 or "@" not in table[EMAIL_INDEX] or "." not in table[EMAIL_INDEX] or table[SUBSCRIPTION_INDEX] not in ["0","1"]:
        view.print_error_message("The entered data was incorrect!")
    
    crm.create_customer(table)

def update_customer():

    customer_id = view.get_input("Please input user ID")
    table = crm.TABLE

    if crm.is_id_in_base(customer_id):
        [table[NAME_INDEX], table[EMAIL_INDEX], table[SUBSCRIPTION_INDEX]] = view.get_inputs("Please provide name, email and subscription status")
        crm.update_customers(customer_id, table)
    else:
        view.print_error_message("There is no such id in the base.")

def delete_customer():
    customer_id = view.get_input("Please input user ID")
    deleted_id = crm.delete_customer(customer_id)
    view.print_message(deleted_id)
    

def get_subscribed_emails():
    subscribed_emails_list = crm.get_emails_of_subscribent()

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
