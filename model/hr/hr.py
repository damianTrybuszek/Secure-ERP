""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
from model import data_manager, util

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

ID_INDEX = 0
NAME_INDEX = 1
DATE_OF_BIRTH = 2
DEPARTMENT = 3
CLEARANCE_LEVEL = 4


TABLE = ["","","","",""]

EMPLOYEES = data_manager.read_table_from_file(DATAFILE, separator=';') 


def get_employees():
    
    return data_manager.read_table_from_file(DATAFILE, separator=';')

def add_employee():

    data_manager.write_table_to_file(DATAFILE, EMPLOYEES, separator=';')

def create_employee(TABLE):
    TABLE[ID_INDEX] = util.generate_id()
    EMPLOYEES.append(TABLE)
    add_employee()

def is_id_in_base(id):
    for element in EMPLOYEES:
        if element[ID_INDEX] == id:
            return True
    return False

def update_employee(id,TABLE):
    for element in EMPLOYEES:
        if element [ID_INDEX] == id:
            element[NAME_INDEX] = TABLE[NAME_INDEX]
            element[DATE_OF_BIRTH] = TABLE[DATE_OF_BIRTH]
            element[DEPARTMENT] = TABLE[DEPARTMENT]
            element[CLEARANCE_LEVEL] = TABLE[CLEARANCE_LEVEL]
            add_employee()
            return ("EMPLOYEE has updated")

def delete_employee(id):
    for element in EMPLOYEES:
        if element[ID_INDEX] == id:
            EMPLOYEES.remove(element)
            add_employee()
            return ("EMPLOYEE has deleted")
    return ("There is no ID in the base")



