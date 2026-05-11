def curry(func):
    count = func.__code__.co_argcount

    def accumulator(args):
        # Base Case: We have all the arguments
        if len(args) == count:
            return func(*args)

        # Recursive Step: Return a function that calls
        # accumulator again with one more argument
        return lambda x: accumulator(args + [x])

    return accumulator([])
