def print_menu(title, list_options):

    print(f"\n{title}\n")
    for i in range(1, len(list_options)):
        print(f"({i}) {list_options[i]}")
    print(f"(0) {list_options[0]}")

    # Args:
    #     title (str): the title of the menu (first row)
    #     list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)



def print_message(message):
    print(f"\n{message} \n")


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass

# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    pass


def get_input(label):
    user_input = input(f"\n{label}: ")
    return user_input


def get_inputs(labels):
    user_input = input(f"\n{labels}: ")
    return user_input


def print_error_message(message):
    print(f"\n{message} \n")

