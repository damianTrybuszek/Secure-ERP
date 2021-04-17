import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    id_list = []

    for i in range(10):
        if i in range(0,4):
            id_list.append(random.choice(string.ascii_lowercase))
        if i in range(4,6):
            id_list.append(random.choice(string.ascii_uppercase))
        if i in range(6,8):
            id_list.append(random.choice(string.digits))
        if i in range(8,10):
            id_list.append(random.choice(allowed_special_chars))
        
    id = []
    for _ in range(10):
        temp_elem = random.choice(id_list)
        id_list.remove(temp_elem)
        id.append(temp_elem)
        
    return (''.join(id))
