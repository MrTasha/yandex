#A
from sys import stdin
print(sum(map(int, stdin.read().split())))    


#B
from sys import stdin
print(round(sum(x := [int(i.split()[2]) - int(i.split()[1]) for i in stdin.readlines()]) / len(x)))


#C
from sys import stdin
for i in stdin.readlines():
    if not i.startswith('#'):
        print(i[:i.find('#')])


#D
from sys import stdin
for line in (x := [i.strip() for i in stdin])[:-1]:
    if x[-1].lower() in line.lower():
        print(line)


#E
from sys import stdin
data = [string.strip().split() for string in stdin]
words = []
for line in data:
    words.extend(line)
for word in sorted(set(words)):
    if word.lower() == word.lower()[::-1]:
        print(word)


#F
LITER = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}
data, translit_data = '', ''
with open("cyrillic.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        data += line

for i in data:
    if i.upper() in LITER:
        translit_data += LITER[i.upper()].lower().capitalize() if i == i.upper() else LITER[i.upper()].lower()
    else:
        translit_data += i
with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    print(translit_data, file=file_out)


#G
name = input()
numbers = []
with open(name, 'r') as f:
    for line in f:
        numbers.extend([int(x) for x in line.split()])
print(len(numbers))
print(len(list(filter(lambda x: x > 0, numbers))))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers), 2))


#H
files_in = input(), input()
file_out = input()
words = [set(), set()]
for i in range(len(files_in)):
    with open(files_in[i], 'r') as file_in:
        for line in file_in:
            words[i].update({x for x in line.split()})
with open(file_out, 'w') as file_out:
    for word in sorted(words[0].symmetric_difference(words[1])):
        print(word, file=file_out)


#ЗI
first_file, second_file = input(), input()
data = []
with open(first_file, 'r') as f:
    for line in f:
        data.append(line.strip().replace('\t', '').split())
data = [i for i in data if any(i)]
with open(second_file, 'w') as g:
    for line in data:
        print(' '.join(line), file=g)


#J
file_in, number = input(), int(input())
data = []
with open(file_in) as f:
    for line in f:
        data.append(line)
for line in data[-number:]:
    print(line.strip())