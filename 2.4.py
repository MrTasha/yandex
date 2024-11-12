#A

dim = int(input())
for i in range(dim):
    for j in range(dim):
        print((i + 1) * (j + 1), end=' ')
    print()

#B

dim = int(input())
for i in range(1, dim + 1):
    for j in range(1, dim + 1):
        print(f'{j} * {i} = {i * j}')

#C

size = int(input())
print(1)
last_len = 1
current_len = 0
for num in range(2, size + 1):
    if current_len > last_len:
        last_len = current_len
        current_len = 0
        print('')
    print(num, end=' ')
    current_len += 1

#D

c = int(input())
s = 0
for _ in range(c):
    n = int(input())
    while n > 0:
        s += n % 10
        n //= 10

print(s) 

#E

n = int(input())
b = 0
for _ in range(n):
    c = False
    while (s := input()) != 'ВСЁ':
        if s == 'зайка' and c is False:
            b = b + 1
            c = True

print(b)

#F

n = int(input())
a = int(input())
for _ in range(0, n - 1):
    b = int(input())
    while a != 0:
        if a < b:
            a, b = b, a
        a = a % b
    a = b
print(a)

#G

n = int(input())
for i in range(n):
    for j in range(3 + i, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i + 1}!!!')

#H

c = int(input())
bn = ' '
bs = 0
for i in range(c):
    name = input()
    n = int(input())
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s >= bs:
        bs = s
        bn = name
print(bn)

#I

c = int(input())
r = 0
for _ in range(c):
    n = int(input())
    m = -1
    while n > 0:
        if n % 10 > m:
            m = n % 10
        n //= 10
    r = r * 10 + m
print(r)
#J

sl = int(input())
print('А Б В')
for a in range(1, sl + 1):
    for b in range(1, sl + 1):
        for c in range(1, sl + 1):
            if a + b + c == sl:
                print(a, b, c)

