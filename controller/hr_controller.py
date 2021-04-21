from model.hr import hr
from view import terminal as view
from model import data_manager
from model import util

ID_INDEX = 0
NAME_INDEX = 1
DATE_OF_BIRTH = 2
DEPARTMENT = 3
CLEARANCE_LEVEL = 4

def list_employees():
    employee_list = hr.get_employees()
    view.print_table(employee_list, hr.HEADERS)


def add_employee():
    table = hr.TABLE

    [table[NAME_INDEX], table[DATE_OF_BIRTH], table[DEPARTMENT], table[CLEARANCE_LEVEL]] = view.get_inputs("Please provide name, date of birth, department and clearance level : ")
    #ADD CONDITIONS

    hr.create_employee(table)


def update_employee():

    employee_id = view.get_input("Please input user ID")
    table = hr.TABLE

    if hr.is_id_in_base(employee_id):
        [table[NAME_INDEX], table[DATE_OF_BIRTH], table[DEPARTMENT], table[CLEARANCE_LEVEL]] = view.get_inputs("Please provide name, date of birth, department and clearance level : ")
        hr.update_employee(employee_id, table)
    else:
        view.print_error_message("There is no such id in the base.")



def delete_employee():
    employee_id = view.get_input("Please input user ID")
    deleted_id = hr.delete_employee(employee_id)
    view.print_message(deleted_id)



def get_oldest_and_youngest():
    table = hr.TABLE
    employees = hr.EMPLOYEES 
    
    name_of_oldest_user = []
    year_of_oldest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[0])
    month_of_oldest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[1])
    day_of_oldest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[2])


    for employee in employees:
        if int(((employee[DATE_OF_BIRTH]).split("-"))[0]) < year_of_oldest:
            name_of_oldest_user[0] = employee[ID_INDEX]
            year_of_oldest = int(((employee[DATE_OF_BIRTH]).split("-"))[0])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) < month_of_oldest:
            name_of_oldest_user[0] = employee[ID_INDEX]
            month_of_oldest = int(((employee[DATE_OF_BIRTH]).split("-"))[1])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) < day_of_oldest:
            name_of_oldest_user[0] = employee[ID_INDEX]
            day_of_oldest = int(((employee[DATE_OF_BIRTH]).split("-"))[2])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) == day_of_oldest:
            name_of_oldest_user.append(employee[ID_INDEX])

    name_of_youngest_user = []
    year_of_youngest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[0])
    month_of_youngest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[1])
    day_of_youngest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[2])


    for employee in employees:
        if int(((employee[DATE_OF_BIRTH]).split("-"))[0]) > year_of_youngest:
            name_of_youngest_user[0] = employee[ID_INDEX]
            year_of_youngest = int(((employee[DATE_OF_BIRTH]).split("-"))[0])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) > month_of_youngest:
            name_of_youngest_user[0] = employee[ID_INDEX]
            month_of_youngest = int(((employee[DATE_OF_BIRTH]).split("-"))[1])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) > day_of_youngest:
            name_of_youngest_user[0] = employee[ID_INDEX]
            day_of_youngest = int(((employee[DATE_OF_BIRTH]).split("-"))[2])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) == day_of_youngest:
            name_of_youngest_user.append(employee[ID_INDEX])

    view.print_general_results(name_of_oldest_user, "id of oldest user: ")
    view.print_general_results(name_of_youngest_user, "id of youngest user: ")



def get_average_age():
    current_year = 2021
    table = hr.TABLE
    employees = hr.EMPLOYEES
    list_of_age = []
    sum_of_age = 0

    for employee in employees:
        list_of_age.append(current_year - int(((employee[DATE_OF_BIRTH]).split("-"))[0]))

    for element in list_of_age:
        sum_of_age += element
    
    average_age = sum_of_age / len(list_of_age)

    view.print_general_results(average_age, "average age is: ")
    

def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
