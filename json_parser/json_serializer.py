def to_string(input_object):

    if input_object is not dict:
        try:
            input_object = vars(input_object)
        except TypeError:
            pass

    def inner(json):
        json_type = type(json)

        if json_type is dict:
            string = '{'
            dict_len = len(json)
            for i, (key, val) in enumerate(json.items()):
                string += '"{}": {}'.format(key, to_string(val))

                if i < dict_len - 1:
                    string += ', '
                else:
                    string += '}'
            return string

        elif json_type is list:
            string = '['
            list_len = len(json)
            for i, val in enumerate(json):
                string += to_string(val)
                if i < list_len - 1:
                    string += ', '
                else:
                    string += ']'
            return string

        if json_type is tuple:
            string = '['
            list_len = len(json)
            for i, val in enumerate(json):
                string += to_string(val)
                if i < list_len - 1:
                    string += ', '
                else:
                    string += ']'
            return string

        elif json_type is str:
            return '"{}"'.format(json)

        elif json_type is bool:
            return "true" if json else "false"

        elif json is None:
            return "null"

        return str(json)

    return inner(input_object)