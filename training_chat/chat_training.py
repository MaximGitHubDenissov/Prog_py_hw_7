from tkinter import*
from tkinter import ttk
import json
from PIL import Image


def save_results(record):
    with open('results.json', 'w', encoding='utf-8') as file:
        json.dump(record,file)
def load_results():
    with open('results.json', 'r', encoding='utf-8') as file:
        lst = json.load(file)
        return lst
results = load_results()


def finish():
    root.destroy()
    print("Завершение работы приложения")


def add_record():
    def show_res():
        my_list = ['0', '0', '0']
        my_list[0] = one_entry.get()
        my_list[1] = two_entry.get()
        my_list[2] = three_entry.get()
        add_window.destroy()
        global results
        results.append(my_list)
        save_results(results)
    add_window = Tk()
    add_window.title('Добавить результат')
    add_window.geometry("500x470")
    welcome_label = Label(add_window, text="Запиши результаты тренировок и нажми конопку ОК", font=('Arial', 14), foreground='red')
    welcome_label.pack()
    one_entry = Entry(add_window, width=10)
    one_entry.place(x=400,y=50)
    one_label = Label(add_window, text='Подтягивания', font=('Arial',12))
    one_label.place(x=50, y=50)
    two_entry = Entry(add_window, width=10)
    two_entry.place(x=400,y=75)
    two_label = Label(add_window, text='Приседания', font=('Arial',12))
    two_label.place(x=50, y=75)
    three_entry = Entry(add_window, width=10)
    three_entry.place(x=400,y=100)
    three_label = Label(add_window, text='Жим штанги лежа', font=('Arial',12))
    three_label.place(x=50, y=100)
    OK_button = Button(add_window, text='OK', command=show_res)
    OK_button.place(x=50,y=200)
    
    

def show_result():
    show_window = Tk()
    show_window.title('Результаты Ваших тренировок')
    show_window.geometry("700x500")
    columns = ('first', 'second', 'third')
    tree = ttk.Treeview(show_window, columns=columns, show='headings')
    tree.pack(fill=BOTH, expand=1)
    tree.heading('first', text='Подтягивания')
    tree.heading('second', text='Приседания')
    tree.heading('third', text='Жим штанги лежа')
    results = load_results()
    for elm in results:
        tree.insert("", END,values=elm)
    


root = Tk()
root.title('Приложение для тренировок')

root.geometry("500x470")

label = Label(text="Привет!\n в этом приложении ты можешь \nзаписывать \
результаты своих тренировок\n и отслеживать прогресс", font=('Arial', 12))

photo = PhotoImage(file='add.png')
add_label = Label(image=photo )  

photo2 = PhotoImage(file='progress.png')
prog_label = Label(image=photo2)

label.pack()

add_label.place(x=400,y=100)
prog_label.place(x=400,y=210)

root.resizable(False,False)
icon = PhotoImage(file='icon.png')
root.iconphoto(True,icon)

add_but = Button(text='Добавить результаты тренировок',command=add_record, font=("Arial", 12), background='lightblue')
show_but = Button(text='Посмотреть свой прогресс', command=show_result, font=("Arial", 12), background='lightblue')
add_but.place(x=20, y=150, anchor=W,  width=350,height=100)
show_but.place(x=20, y=250, anchor=W,  width=350,height=100)



root.protocol('WM_DELETE_WINDOW', finish)

root.mainloop()
