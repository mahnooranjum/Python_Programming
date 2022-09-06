from textwrap import wrap


def mydecor(function):
    def wrapper(*args, **kwargs):
        rval = function(*args, **kwargs)
        print("I am decorating your function")
        return rval

    return wrapper


@mydecor
def hello_world(name):
    print(f"hello {name}")
    return f"hello {name}"



print(hello_world("name"))