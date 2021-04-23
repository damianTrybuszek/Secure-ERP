from model.hr import hr
from view import terminal as view


ID_INDEX = 0
NAME_INDEX = 1
DATE_OF_BIRTH = 2
DEPARTMENT = 3
CLEARANCE_LEVEL = 4
DATE = 5

def list_employees():
    employee_list = hr.get_employees()
    view.print_table(employee_list, hr.HEADERS)


def add_employee():
    table = ["","Please provide name","Please provide date of birth like YYYY-MM-DD","Please input your department","Please input Clearance status"]

    [table[NAME_INDEX], table[DATE_OF_BIRTH], table[DEPARTMENT], table[CLEARANCE_LEVEL]] = view.get_inputs( [table[NAME_INDEX], table[DATE_OF_BIRTH], table[DEPARTMENT], table[CLEARANCE_LEVEL]])
    #ADD CONDITIONS

    hr.create_employee(table)


def update_employee():

    employee_id = view.get_input("Please input user ID")
    table = ["","Please provide name","Please provide date of birth like YYYY-MM-DD","Please input your department","Please input Clearance status"]

    if hr.is_id_in_base(employee_id):
        [table[NAME_INDEX], table[DATE_OF_BIRTH], table[DEPARTMENT], table[CLEARANCE_LEVEL]] = view.get_inputs( [table[NAME_INDEX], table[DATE_OF_BIRTH], table[DEPARTMENT], table[CLEARANCE_LEVEL]])
        hr.update_employee(employee_id, table)
    else:
        view.print_error_message("There is no such id in the base.")



def delete_employee():
    employee_id = view.get_input("Please input user ID")
    deleted_id = hr.delete_employee(employee_id)
    view.print_message(deleted_id)



def get_oldest_and_youngest():
    employees = hr.EMPLOYEES 
    
    name_of_oldest_user = []
    year_of_oldest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[0])
    month_of_oldest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[1])
    day_of_oldest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[2])


    for employee in employees:
        if int(((employee[DATE_OF_BIRTH]).split("-"))[0]) < year_of_oldest:
            name_of_oldest_user[0] = employee[NAME_INDEX]
            year_of_oldest = int(((employee[DATE_OF_BIRTH]).split("-"))[0])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) < month_of_oldest:
            name_of_oldest_user[0] = employee[NAME_INDEX]
            month_of_oldest = int(((employee[DATE_OF_BIRTH]).split("-"))[1])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) < day_of_oldest:
            name_of_oldest_user[0] = employee[NAME_INDEX]
            day_of_oldest = int(((employee[DATE_OF_BIRTH]).split("-"))[2])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_oldest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) == day_of_oldest:
            name_of_oldest_user.append(employee[NAME_INDEX])

    name_of_youngest_user = []
    year_of_youngest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[0])
    month_of_youngest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[1])
    day_of_youngest = int(((employees[0][DATE_OF_BIRTH]).split("-"))[2])


    for employee in employees:
        if int(((employee[DATE_OF_BIRTH]).split("-"))[0]) > year_of_youngest:
            name_of_youngest_user[0] = employee[NAME_INDEX]
            year_of_youngest = int(((employee[DATE_OF_BIRTH]).split("-"))[0])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) > month_of_youngest:
            name_of_youngest_user[0] = employee[NAME_INDEX]
            month_of_youngest = int(((employee[DATE_OF_BIRTH]).split("-"))[1])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) > day_of_youngest:
            name_of_youngest_user[0] = employee[NAME_INDEX]
            day_of_youngest = int(((employee[DATE_OF_BIRTH]).split("-"))[2])
        elif int(((employee[DATE_OF_BIRTH]).split("-"))[0]) == year_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[1]) == month_of_youngest and int(((employee[DATE_OF_BIRTH]).split("-"))[2]) == day_of_youngest:
            name_of_youngest_user.append(employee[NAME_INDEX])
    
    oldest_and_youngest = tuple(name_of_oldest_user)
    oldest_and_youngest += tuple(name_of_youngest_user)
    print(oldest_and_youngest)
    view.print_general_results(oldest_and_youngest, "name of oldest and youngest user: ")
    # view.print_general_results(name_of_youngest_user, "name of youngest user: ")



def get_average_age():
    current_year = 2021
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
    employees = hr.EMPLOYEES
    date_within_two_weeks = []
    coming_birthday_names = []
    user_input_date = view.get_input("Please input the date like : MM-DD")

    month = int(((user_input_date).split("-"))[0])
    day = int(((user_input_date).split("-"))[1])

    if month in range(1,13) and day in range(1,32):

        for _ in range(14):
            date = (f"{str(month).zfill(2)}-{str(day).zfill(2)}")
            date_within_two_weeks.append(date)

            if day == 31:
                if month == 12:
                    month = 1
                    day = 1
                else:
                    day = 1
                    month += 1
            else:
                day += 1
        
        for employee in employees:

            month_of_birth = int(((employee[DATE_OF_BIRTH]).split("-"))[1])
            day_of_birth = int(((employee[DATE_OF_BIRTH]).split("-"))[2])
            date = (f"{str(month_of_birth).zfill(2)}-{str(day_of_birth).zfill(2)}")
            if date in date_within_two_weeks:
                coming_birthday_names.append(employee[NAME_INDEX])
    

    
        if len(coming_birthday_names) > 0:
            view.print_general_results(coming_birthday_names, "Names of employees having birthdays within the two weeks")
        else:
            view.print_error_message("Nobody has birthday within two weeks")
    else:
        view.print_error_message("The input date is not correct")

            

def count_employees_with_clearance():
    employees = hr.EMPLOYEES
    least_clearance = employees[0][CLEARANCE_LEVEL] 
    counter = 0
    for employee in employees:
        if employee[CLEARANCE_LEVEL] < least_clearance:
            least_clearance = employee[CLEARANCE_LEVEL]
    
    for employee in employees:
        if employee[CLEARANCE_LEVEL] == least_clearance:
            counter += 1

    view.print_general_results(counter, "number of employees with at least clearance level")


def count_employees_per_department():
    employees = hr.EMPLOYEES

    department_dict = {}

    for employee in employees:
        department_dict.update({employee[DEPARTMENT]: 0})

    for employee in employees:
        department_dict[employee[DEPARTMENT]] += 1

    view.print_general_results(department_dict, "number of departments")
    



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
