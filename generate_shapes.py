import numpy as np

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
        translateY = np.random.randint(0,200)
    return {
            'scaleX': scaleX,
            'scaleY': scaleY,
            'translateX': translateX,
            'translateY': translateY,
            'unit': 'PT',
            }


def _get_generic_object(objectId, pageId, shapeType, height=None, width=None, **kwargs):
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

def _color_picker():
    colors = [ '1,0,0',
               '0,1,0',
               '0,0,1',
               '1,1,0',
               '1,0,1',
               '0,1,1',
               ]
    color = [int(x) for x in np.random.choice(colors).split(',')]
    return {'solidFill': {'color': {'rgbColor': {'red': color[0], 'green': color[1], 'blue': color[2]}}}}

def update_object_color(objectId):
    return {
            'updateShapeProperties': {
                'objectId': objectId,
                'fields':'shapeBackgroundFill.solidFill.color',
                'shapeProperties': {
                    'shapeBackgroundFill': _color_picker()
                    }
                }
            }

def add_star(**kwargs):
    shapeType = np.random.choice(['STAR_12', 'STAR_16', 'STAR_24', 'STAR_32', 'STAR_5', 'SUN',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_n_agon(**kwargs):
    shapeType = np.random.choice(['TRAPEZOID', 'HEXAGON', 'HEPTAGON', 'OCTAGON', 'DECAGON', 'DODECAGON',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_rectangle_or_circles(**kwargs):
    shapeType = np.random.choice(['RECTANGLE','ROUND_RECTANGLE','ELLIPSE', 'PIE', 'CUBE',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_arrows(**kwargs):
    shapeType = np.random.choice(['BENT_UP_ARROW', 'QUAD_ARROW', 'UTURN_ARROW', 'DOWN_ARROW_CALLOUT'])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_braces(**kwargs):
    shapeType = np.random.choice(['BRACE_PAIR', 'BRACKET_PAIR',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_cees(**kwargs):
    shapeType = np.random.choice(['CAN', 'CHEVRON', 'CLOUD',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_math(**kwargs):
    shapeType = np.random.choice(['MATH_DIVIDE', 'MATH_EQUAL ''MATH_NOT_EQUAL', 'MATH_PLUS',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_irregular(**kwargs):
    shapeType = np.random.choice(['IRREGULAR_SEAL_1', 'IRREGULAR_SEAL_2', 'LIGHTNING_BOLT',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

def add_rest(**kwargs):
    shapeType = np.random.choice(['DOUBLE_WAVE', 'HEART', 'NO_SMOKING', 'TEARDROP', 'DONUT', 'HOME_PLATE', 'PLAQUE', 'RIBBON', 'SPEECH', 'STARBURST',])
    return _get_generic_object(shapeType=shapeType, **kwargs)

func_dict = {
        'STAR': add_star,
        'NAGON': add_n_agon,
        'RECT_OR_CIRC': add_rectangle_or_circles,
        'ARROW': add_arrows,
        'BRACES': add_braces,
        'CEES': add_cees,
        'MATH': add_math,
        'IRREGULAR': add_irregular,
        'REST': add_rest,
        }

def random_add_shape(**kwargs):
    func = np.random.choice(list(func_dict.values()))
    return func(**kwargs)

def add_specific_shape(shape_name, **kwargs):
    func = func_dict[shape_name]
    return func(**kwargs)

def add_text_box(**kwargs):
    return _get_generic_object(shapeType='TEXT_BOX', **kwargs)
