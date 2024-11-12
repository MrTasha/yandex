#A

print('Как Вас зовут?')
name = input()
print(f'Здравствуйте, {name}!')
print('Как дела?')
answ = input()

if answ == 'хорошо':
    print('Я за вас рада!')
if answ == 'плохо':
    print('Всё наладится!')

#B

p = int(input())
v = int(input())

if p > v:
    print('Петя')
elif p < v:
    print('Вася')

#C

p = int(input())
v = int(input())
t = int(input())

if v > p and v > t:
    print('Вася')
elif p > v and p > t:
    print('Петя')
elif t > v and t > p:
    print('Толя')

#D

p = int(input())
v = int(input())
t = int(input())

if v > p and v > t:
    print('1. Вася')
elif p > v and p > t:
    print('1. Петя')
elif t > p and t > v:
    print('1. Толя')

if t > v > p or p > v > t:
    print('2. Вася')
elif t > p > v or v > p > t:
    print('2. Петя')
elif p > t > v or v > t > p:
    print('2. Толя')

if v < p and v < t:
    print('3. Вася')
elif p < v and p < t:
    print('3. Петя')
elif t < v and t < p:
    print('3. Толя')

#E

ap = int(input())
av = int(input())
p = 7 - 3 + 2 + ap
v = 6 + 3 + 5 - 2 + av

if p > v:
    print('Петя')
elif v > p:
    print('Вася')

#F

y = int(input())
if y % 4 or not y % 100 and y % 400:
    print('NO')
else:
    print('YES')

#G

n = int(input())

if n // 1000 == n % 10 and n % 1000 // 100 == n % 100 // 10:
    print('YES')
else:
    print('NO')

#H

nat = input()
if 'зайка' in nat:
    print('YES')
else:
    print('NO')

#I

f = input()
s = input()
t = input()

if f < s and f < t:
    print(f)
elif s < f and s < t:
    print(s)
elif t < f and t < s:
    print(t)

#J

n = int(input())

s1 = n // 10 % 10 + n % 10
s2 = n // 100 % 10 + n // 10 % 10

if s1 < s2:
    print(str(s2) + str(s1))
else:
    print(str(s1) + str(s2))