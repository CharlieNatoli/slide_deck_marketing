import numpy as np

def add_bluh(s):
    return ', bluh.'.join(s.split('.'))


def add_bruh(s):
    return ', bruh.'.join(s.split('.'))

def mockbob_string(s):
    return_string = ''
    force_lowercase = True
    force_uppercase = False
    for i in range(len(s)):
        if s[i].isalpha():
            if force_lowercase:
                return_string += s[i].lower()
                force_lowercase = False
                force_uppercase = True
            elif force_uppercase:
                return_string += s[i].upper()
                force_uppercase = False
                force_lowercase = True
        else:
            return_string += s[i]
    return return_string


func_list = [
    add_bluh,
    add_bruh,
    mockbob_string
]


def random_parse_string(s):
    func = np.random.choice(func_list)
    return func(s)


def add_text(objectId, text, fontsize=70):
    return [
        {
            'insertText': {
                'objectId': objectId,
                'insertionIndex': 0,
                'text': text
            }
        },{
            'updateTextStyle': {
                'objectId': objectId,
                'textRange': {'type': 'ALL'},
                'style': {
                    'fontFamily':  np.random.choice(['Pacifico', 'Caveat']),
                    'bold': True,
                    'fontSize': {
                        'magnitude': fontsize,
                        'unit': 'PT'
                    },
                    'foregroundColor': {
                        'opaqueColor': {
                            'rgbColor':
                                { 'blue': 0.0, 'green': 0.0,  'red': 0.0} if fontsize==70 else {'blue': 1.0, 'green': 1.0, 'red': 1.0}
                        }
                    }
                },

                'fields': 'foregroundColor,fontFamily,fontSize, bold'
            }
        }
    ]
