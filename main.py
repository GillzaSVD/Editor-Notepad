from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

root = Tk()
root.title('Txt')
f2 = Frame(root, width=100, height=100)
f3 = Frame(root, width=100, height=100)
f2.pack(side=BOTTOM, anchor=W)
f3.pack(side=BOTTOM, anchor=W)
text1 = Text(f2)
text1.pack(side=LEFT)

scroll1 = Scrollbar(f2, command=text1.yview)
scroll1.pack(side=LEFT, fill=Y)

text1.config(yscrollcommand=scroll1.set)

def open_file():
    try:
        file_name = fd.askopenfilename()
        file = open(file_name)
        get = file.read()
        text1.insert(1.0, get)
        file.close()
    except FileNotFoundError:
        mb.showinfo("Внимание", "Файл не загружен")

def save_file():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*")))
    file = open(file_name, 'w')
    get = text1.get(1.0, END)
    file.write(str(get))
    file.close()

def delete_file():
    answer = mb.askyesno("Уверены?", message="Вы хотите удалить текст?")
    if answer == True:
        text1.delete(0.0, END)

but1 = Button(f3, width=20, text='Открыть', command=open_file)
but2 = Button(f3, text='Сохранить', width=20, command=save_file)
but3 = Button(text="Очистить", command=delete_file, width=20)
but1.pack(side=LEFT)
but2.pack(side=LEFT)
but3.pack(side=RIGHT)

mainloop()