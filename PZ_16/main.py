import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#8000FF', bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/add.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить товар', command=self.open_dialog, bg='#8000FF', bd=2,
                                         fg='white', compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.edit_img = tk.PhotoImage(file="img/edit.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#8000FF',
                                    bd=2, fg='white', compound=tk.TOP, image=self.edit_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="img/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#8000FF',
                               bd=2, fg='white', compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="img/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#8000FF',
                               bd=2, fg='white', compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="img/update.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#8000FF',
                                bd=2, fg='white', compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
        'kod', 'mark', 'type', 'cost', 'count', 'zapas'), height=15,
                        show='headings')

        self.tree.column('kod', width=40, anchor=tk.CENTER)
        self.tree.column('mark', width=150, anchor=tk.CENTER)
        self.tree.column('type', width=180, anchor=tk.CENTER)
        self.tree.column('cost', width=80, anchor=tk.CENTER)
        self.tree.column('count', width=150, anchor=tk.CENTER)
        self.tree.column('zapas', width=150, anchor=tk.CENTER)

        self.tree.heading('kod', text='Код')
        self.tree.heading('mark', text='Торговая марка')
        self.tree.heading('type', text='Тип')
        self.tree.heading('cost', text='Цена')
        self.tree.heading('count', text='Количество на складе')
        self.tree.heading('zapas', text='Минимальный запас')

        self.tree.pack()

    def records(self, kod, mark, type, cost, count, zapas):
        self.db.insert_data(kod, mark, type, cost, count, zapas)
        self.view_records()

    def update_record(self, kod, mark, type, cost, count, zapas):
        self.db.cur.execute(
            """UPDATE users SET kod=?, mark=?, type=?, cost=?, count=?, zapas=? WHERE kod=?""",
            (kod, mark, type, cost, count, zapas, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE kod=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, mark):
        mark = (mark,)
        self.db.cur.execute("""SELECT * FROM users WHERE mark=?""", mark)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить товар')
        self.geometry('400x250+400+300')
        self.resizable(False, False)

        label_kod = tk.Label(self, text='Код товара')
        label_kod.place(x=50, y=25)
        self.entry_kod = ttk.Entry(self)
        self.entry_kod.place(x=180, y=25)

        label_mark = tk.Label(self, text='Торговая марка')
        label_mark.place(x=50, y=50)
        self.mark = ttk.Combobox(self, values=[u'Apple', u'Microsoft', u'Intel', u'HyperX',
        u'Sony', u'Corsair', u'AMD', u'HP'])
        self.mark.place(x=180, y=50)

        label_type = tk.Label(self, text='Тип')
        label_type.place(x=50, y=75)
        self.type = ttk.Combobox(self, values=[u'Смартфоны', u'Программное обеспечение', u'Комплектующие для ПК',
        u'Игровые девайсы', u'Телевизоры', u'Процессоры'])
        self.type.place(x=180, y=75)

        label_cost = tk.Label(self, text='Цена')
        label_cost.place(x=50, y=100)
        self.entry_cost = ttk.Entry(self)
        self.entry_cost.place(x=180, y=100)

        label_count = tk.Label(self, text='Количество на складе')
        label_count.place(x=50, y=125)
        self.entry_count = ttk.Entry(self)
        self.entry_count.place(x=180, y=125)

        label_zapas = tk.Label(self, text='Минимальный запас')
        label_zapas.place(x=50, y=150)
        self.entry_zapas = ttk.Entry(self)
        self.entry_zapas.place(x=180, y=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_kod.get(),
                                                                       self.mark.get(),
                                                                       self.type.get(),
                                                                       self.entry_cost.get(),
                                                                       self.entry_count.get(),
                                                                       self.entry_zapas.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_kod.get(),
                                                                          self.mark.get(),
                                                                          self.type.get(),
                                                                          self.entry_cost.get(),
                                                                          self.entry_count.get(),
                                                                          self.entry_zapas.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)
        self.mark_search = ttk.Combobox(self,
                                        values=[u'Apple', u'Microsoft', u'Intel', u'HyperX',
                                        u'Sony', u'Corsair', u'AMD', u'BUD'])
        self.mark_search.place(x=60, y=20, width=200)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=70, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.mark_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('Tovar_zapas.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                kod INTEGER PRIMARY KEY AUTOINCREMENT,
                mark TEXT,
                type TEXT NOT NULL,
                cost INTEGER,
                count INTEGER,
                zapas INTEGER
                )""")

    def insert_data(self, kod, mark, type, cost, count, zapas):
        self.cur.execute(
            """INSERT INTO users(kod, mark, type, cost, count, zapas) VALUES (?, ?, ?, ?, ?, ?)""",
            (kod, mark, type, cost, count, zapas))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Товарный запас")
    root.geometry("1000x450+300+200")
    root.resizable(False, False)
    root.mainloop()
