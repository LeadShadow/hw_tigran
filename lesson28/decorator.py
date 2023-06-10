def input_error(func):
    def wrapper(contacts, *args):
        try:
            result = func(contacts, *args)
        except