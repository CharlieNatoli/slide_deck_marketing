import numpy as np


def add_star(*args, **kwargs):
    pass

def add_decagon(*args, **kwargs):
    pass


func_list = [
        add_star,
        add_decagon,
        ]

def random_add_shape(*args, **kwargs):
    func = np.random.choice(func_list)
    return func(*args, **kwargs)
