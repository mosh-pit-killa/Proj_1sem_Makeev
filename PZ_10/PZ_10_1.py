# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого максимального элемента:
# Произведение элементов средней трети:

a = ['7 -99 6 12 -36 20 45 100 -15']
f1 = open('data_1.txt', 'w', encoding='UTF-8')
f1.writelines(a)
f1.close()

f2 = open('data_2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(a)
f2.close()

f1 = open('data_1.txt', encoding='UTF-8')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f1 = open('data_1.txt', encoding='UTF-8')
a = [7, -99, 6, 12, -36, 20, 45, 100, -15]
maxi = a[0]
for i, v in enumerate(a):
    if maxi < v:
        maxi = i
f2 = open('data_2.txt', 'a', encoding='UTF-8')
f2.write('\n')
print('Количество элементов: ', len(k), file=f2)
print('Индекс первого максимального элемента: ', maxi, file=f2)

s = 12*-36*20
print('Произведение элементов средней трети: ', s, file=f2)
f2.close()
