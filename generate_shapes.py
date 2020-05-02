import numpy as np
import json

def _get_size_blob(size):
    return { 'magnitude': size,
            'unit': 'PT',
            }

def _get_transform_blob(scaleX=None, scaleY=None, translateX=None, translateY=None, **kwargs):
    if scaleX is None:
        scaleX = 3*np.random.rand()

    if scaleY is None:
        scaleY = 3*np.random.rand()

    if translateX is None:
        translateX = np.random.randint(0,500)

    if translateY is None:
        translateY = np.random.randint(0,500)
    return {
            'scaleX': scaleX,
            'scaleY': scaleY,
            'translateX': translateX,
            'translateY': translateY,
            'unit': 'PT',
            }


def _get_generic_shape(objectId, pageId, shapeType, height=None, width=None, **kwargs):
    if height is None:
        height = np.random.randint(1,100)
    if width is None:
        width = np.random.randint(1,100)

    return {
        'createShape': {
        'objectId': objectId,
        'shapeType': shapeType,
        'elementProperties': {
            'pageObjectId': pageId,
            'size': {
                'height': _get_size_blob(height),
                'width': _get_size_blob(width),
                },
            'transform': _get_transform_blob(**kwargs),
            }
        }
    }

def add_star(**kwargs):
    shapeType = np.random.choice(['STAR_12', 'STAR_16', 'STAR_24', 'STAR_32', 'STAR_5', 'SUN',])
    return _get_generic_shape(shapeType=shapeType, **kwargs)

def add_n_agon(**kwargs):
    shapeType = np.random.choice(['TRAPEZOID', 'PARALELOGRAM', 'HEXAGON', 'HEPTAGON', 'OCTAGON', 'DECAGON', 'DODECAGON',])
    return _get_generic_shape(shapeType=shapeType, **kwargs)


func_list = [
        add_star,
        add_n_agon,
        ]

def random_add_shape(**kwargs):
    func = np.random.choice(func_list)
    return json.dumps(func(**kwargs))

def add_text_box(**kwargs):
    return _get_generic_shape(shapeType='TEXT_BOX', **kwargs)
