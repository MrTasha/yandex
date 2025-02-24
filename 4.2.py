#A

def make_list(length, value=0):
    sps = []
    for _ in range(length):
        sps.append(value)
    return sps

#B

def make_matrix(size, value=0):
    if type(size) is int:
        return [[value for i in range(size)] for j in range(size)]
    else:
        return [[value for i in range(size[0])] for j in range(size[1])]

#C

def gcd(*num):
    fst, *others = num
    for snd in others:
        while snd:
            fst, snd = snd, fst % snd
    return fst

#D

def month(n, lng='ru'):
    months = {'en': ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December'], 
              'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                     'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']}
    return months[lng][n - 1]

#E

def to_string(*data, sep=' ', end='\n'):
    return sep.join(str(i) for i in data) + end