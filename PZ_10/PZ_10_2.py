# Из предложенного текстового файла (text18-13.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно вставив после строки N (N – задается пользователем)
# произвольную фразу.

f1 = open('text18-13.txt', encoding='UTF-16')
for i in open('text18-13.txt', encoding='UTF-16'):
    print(i)

a = f1.read()
print('Количество символов в тексте: ', len(a))
f1.close()

f1 = open('text18-13.txt', encoding='UTF-16')
l = f1.readlines()
f1.close()

f1 = open('text18-13.txt', encoding='UTF-16')
f2 = open('data_3.txt', 'w', encoding='UTF-16')
a = f1.readlines()
lenList = int(len(a))

i = 0
randomText = 'Произвольная фраза)'
while i <= lenList - 1:
    f2.writelines(a[i])
    print(a[i])
    if i == 4:
        f2.writelines('{}\n'.format(randomText))
    i += 1
f2.close()
