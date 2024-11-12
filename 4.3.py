#A
def recursive_sum(*args):
    if not args:
        return 0
    return args[0] + recursive_sum(*args[1:])    


#B
def recursive_digit_sum(n):
    return n % 10 + recursive_digit_sum(n // 10) if n else 0


#C
def make_equation(*args):
    if len(args) == 1:
        return str(args[0])
    line = ') * x ' + ('- ' if args[-1] < 0 else '+ ') + str(args[-1])
    return '(' + make_equation(*args[:-1]) + line


#D
def answer(func):
    def wrap(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return wrap


#E
def result_accumulator(func):
    result = []

    def wrap(*args, method="accumulate"):
        result.append(func(*args))
        if method == "drop":
            temp = result.copy()
            result.clear()
            return temp
    return wrap