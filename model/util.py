import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    id_list = []
    id_length = sum([number_of_capital_letters, number_of_small_letters, number_of_digits, number_of_special_chars],0)

    for i in range(id_length):
        if i in range(0,number_of_small_letters):
            id_list.append(random.choice(string.ascii_lowercase))
        elif i in range(number_of_small_letters,number_of_small_letters+number_of_capital_letters):
            id_list.append(random.choice(string.ascii_uppercase))
        elif i in range(number_of_small_letters+number_of_capital_letters,number_of_small_letters+number_of_capital_letters+number_of_digits):
            id_list.append(random.choice(string.digits))
        elif i in range(number_of_small_letters+number_of_capital_letters+number_of_digits,number_of_small_letters+number_of_capital_letters+number_of_digits+number_of_special_chars):
            id_list.append(random.choice(allowed_special_chars))
        
    id = []
    for _ in range(id_length):
        temp_elem = random.choice(id_list)
        id_list.remove(temp_elem)
        id.append(temp_elem)
        
    return (''.join(id))
