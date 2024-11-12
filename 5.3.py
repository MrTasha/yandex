#A
try:
    func()
except Exception as error:
    print(type(error).__name__)
else:
    print('No Exceptions')   


#B
try:
    func('2', None)
except ValueError:
    print('Ура! Ошибка!')


#C
class Broken:
    def __repr__(self):
        raise Exception


try:
    a = Broken()
    func(a)
except Exception:
    print('Ура! Ошибка!')


#D
def only_positive_even_sum(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError
    if not (a > 0 and not a % 2) or not (b > 0 and not b % 2):
        raise ValueError
    return a + b


#E
def merge(a, b):
    try:
        iterator_1 = iter(a)
        iterator_2 = iter(b)
    except TypeError:
        raise StopIteration
    if not (all(isinstance(i, type(a[0])) for i in a) and all(isinstance(i, type(a[0])) for i in b)):
        raise TypeError
    if list(a) != sorted(a) or list(b) != sorted(b):
        raise ValueError
    c = list(a) + list(b)
    c.sort()
    return tuple(c)