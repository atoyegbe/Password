import string
import random


def generate_password(length=12):
    pass_word = string.ascii_letters + string.digits
    pass_word = list(pass_word)
    random.shuffle(pass_word)
    str_p = random.choices(pass_word, k=length)

    return "".join(str_p)