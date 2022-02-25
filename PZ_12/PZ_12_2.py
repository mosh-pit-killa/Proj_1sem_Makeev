# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# Задача взята из ПЗ 7-1
# Дана строка. Подсчитать количество содержащихся в ней цифр.

import tkinter as tk


def numbers():
    s = str(s1.get())
    a = 0
    for i in s:
        if i in '1234567890':
            a += 1
    res.config(text='Количество цифр в строке: {}'.format(a))


root = tk.Tk()
root.geometry('200x100')
root.configure(bg='#2e3138')
root.title('PZ_12_2')
res = tk.Label(root, text='Введите произвольную строку:', bg='#2e3138', fg='#9197a5')
res.pack()
s1 = tk.Entry(root, bg='#444853', fg='white')
s1.pack()
res = tk.Label(root, text='Результат:', bg='#2e3138', fg='#9197a5')
res.pack()
button = tk.Button(root, text='Подсчитать кол-во цифр', command=numbers, bg='#32acdf', fg='white')
button.pack()
root.mainloop()
