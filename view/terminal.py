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
# \--------------------------------/
def print_table(table, headers):

    longest_words = []

    for i in range(len(headers)): 
        longest_words.append(headers[i])
    
    for element in table:
        for i in range(len(element)):
            if len(element[i]) > len(str(longest_words[i])):
                longest_words[i] = element[i]

    cols_width = ["|"]

    for element in longest_words:
        cols_width.append(((len(str(element)))+4)*"-"+"|")

    sum_counters = -2
    
    for element in cols_width:
        sum_counters += len(str(element))

    rows = []
    row_second = ["|"]

    for i  in range(len(headers)):
        temp_width_headers = len(str(longest_words[i]))-len(str(headers[i]))
        row_second.append("  "+headers[i]+(temp_width_headers*" ")+"  |")
    rows.append(row_second)

    for element in table:
        row_second = ["|"]
        for i in range(len(element)):
            temp_width_elements = len(str(longest_words[i]))-len(str(element[i]))
            row_second.append("  "+element[i]+(temp_width_elements*" ")+"  |")
        rows.append(row_second)
        
    print("/"+(sum_counters*"-")+"\\")
    for i in range(len(rows)):
        if i != 0:
            print(''.join(cols_width))
        print(''.join(rows[i]))
    print("\\"+(sum_counters*"-")+"/")


def get_input(label):
    user_input = input(f"\n{label}: ")
    return user_input


def get_inputs(labels):
    
    user_inputs = input(f"\n{labels}: ")
    return user_inputs


def print_error_message(message):
    print(f"\n{message} \n")

