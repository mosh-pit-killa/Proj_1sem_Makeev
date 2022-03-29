# В строках исходного текстового файла (dates1.txt) все даты представить в виде
# подстроки. Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

import re

s = re.compile('\d{2}.\d[02].\d{4}')

with open('dates1.txt', 'r', encoding='utf-8') as main:
    r = main.read()
    d = str(re.findall(s, r))

with open('dates1.txt', 'a', encoding='utf-8') as main:
    main.truncate(0)
    a = ', '.join(re.findall(s, r))
    main.write(a)

with open('result', 'w', encoding='utf-8') as res:
    d = ', '.join(re.findall(s, r))
    k = d.replace('.', '/')
    res.write(k)
