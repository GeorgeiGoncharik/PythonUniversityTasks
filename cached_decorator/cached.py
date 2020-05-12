def cached(function):
    cache = dict()

    def cache_data(*args, **kwargs):
        key = (tuple(args), hash(tuple(sorted(kwargs.items()))))

        if key in cache:
            return cache[key]
        else:
            value = function(*args)
            cache[key] = value
            return value

    return cache_data
