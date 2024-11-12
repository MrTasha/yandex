#A

print("Привет, Яндекс!")

#B

print("Как Вас зовут?")
name = input()
print("Привет,", name)

#C

a = input()
print(f'{a} \n' * 3)

#D

cash = int(input())
price = int(2.5 * 38)
print(cash - price)

#E

c = int(input())
w = int(input())
rub = int(input())
print(rub - c * w)

#F

name = input()
c = int(input())
w = int(input())
rub = int(input())
print("Чек")
print(f'{name} - {w}кг - {c}руб/кг')
print(f'Итого: {w * c}руб')
print(f'Внесено: {rub}руб')
print(f'Сдача: {rub - w * c}руб')

#G

n = int(input())
str = 'Купи слона!\n'
print(f'{str * n}')

#H

a = int(input())
b = input()
print(f'Я больше никогда не буду писать "{b}"! \n' * a)

#I

q = int(input())
c = int(input())
print(int(c * q / 2))

#J

name = input()
code = int(input())

n = code % 10
qro = code // 100
bed = code // 10 % 10

print(f'Группа №{qro}.')
print(f'{n}. {name}.')
print(f'Шкафчик: {code}.')
print(f'Кроватка: {bed}.')