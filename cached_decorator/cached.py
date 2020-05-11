def cached(function):
    cache = dict()

    def cache_data(*args):
        string_args = str(args)

        if string_args in cache:
            return cache[string_args]
        else:
            result = function(*args)
            cache[string_args] = result
            return result

    return cache_data