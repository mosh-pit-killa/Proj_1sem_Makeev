import random

i = int(input('Введите количество строк: '))
j = int(input('Введите количество столбцов: '))

matrix = [[random.randint(-3, 3) for k in range(j)] for i in range(i)]
res1 = [print(matrix[k]) for k in range(i)]

#res2 = [i for i in res1 if i % 2 != 0]

#res3 = [i * 3 for i in res1 if (i%2 != 0)]
#print(res3)
