import random
import string


def alias_generator():
    characters = list(string.ascii_letters + string.digits)
    random.shuffle(characters)
    alias = []
    for i in range(8):
        alias.append(random.choice(characters))
    random.shuffle(alias)
    return "".join(alias)
