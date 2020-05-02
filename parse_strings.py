import numpy as np

def add_bluh(s):
    return ', bluh.'.join(s.split('.'))


def add_bruh(s):
    return ', bruh.'.join(s.split('.'))


func_list = [
        add_bluh,
        add_bruh,
        ]

def random_parse_string(s):
    func = np.random.choice(func_list)
    return func(s)

