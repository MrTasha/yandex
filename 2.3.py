#A

eve = 'Три!'
while input() != eve:
    print('Режим ожидания...')
print('Ёлочка, гори!')

#B

counter = 0
while True:
    inp = input()
    if inp == "Приехали!":
        break
    if "зайка" in inp:
        counter += 1
print(counter)

#C

n = int(input())
k = int(input())
a = ''
for i in range(n, k + 1, 1):
    print(i, end=' ')

#D

start, stop = int(input()), int(input())

step = 1
if stop < start:
    step = -1

for i in range(start, stop + step, step):
    print(i, end=' ')

#E

sum = 0
while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    sum += price

print(sum)

#F

a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a
print(a + b)

#G

a = a1 = int(input())
b = b1 = int(input())
while a != 0:
    a, b = b % a, a
print(a1 * b1 // (a + b))

#H

inf = input()
rep = int(input())
for _ in range(rep):
    print(inf)

#I

a = int(input())
fact = 1
if a == 0:
    print(1)
else:
    for i in range(1, a + 1):
        fact *= i
print(fact)

#J

x, y = 0, 0
while (dir := input()) != 'СТОП':
    n = int(input())
    if dir == 'ВОСТОК':
        x += n
    elif dir == 'ЗАПАД':
        x -= n
    elif dir == 'СЕВЕР':
        y += n
    elif dir == 'ЮГ':
        y -= n
print(y)
print(x)