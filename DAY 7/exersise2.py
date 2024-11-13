def add_100(func):
    def inner_func(*args):
        return func(*args) + 100

    return inner_func


@add_100
def covert_int(value):
    try:
        return int(value)
    except:
        return None


print(covert_int("a"))
