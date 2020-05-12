def to_string(input_object):
    if input_object is not dict:
        try:
            input_object = vars(input_object)
        except TypeError:
            pass

    return parse(input_object)


def parse(arg):
    if isinstance(arg, dict):
        string = '{'
        dict_len = len(arg)
        for i, (key, val) in enumerate(arg.items()):
            string += '"{}": {}'.format(key, to_string(val))

            if i < dict_len - 1:
                string += ', '
            else:
                string += '}'
        return string

    elif isinstance(arg, (list, tuple, set)):
        string = '[' + ', '.join([to_string(a) for a in arg]) + ']'
        return string

    elif isinstance(arg, str):
        return '"{}"'.format(arg)

    elif isinstance(arg, bool):
        return "true" if arg else "false"

    elif arg is None:
        return "null"

    return str(arg)
