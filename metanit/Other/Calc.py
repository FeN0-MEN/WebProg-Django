from math import sqrt
from tkinter import *


def solver(a, b, c):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    # находим дискриминант
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        text = "D = %s \n X1 = %s \n X2 = %s \n" % (D, x1, x2)
    else:
        text = "D = %s \n Корней нет" % D
    return text


def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)


def handler():
    try:
        # make sure that we entered correct values
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Введите a, b, c")


def clear(event):
    caller = event.widget
    caller.delete("0", "end")


# родительский элемент
root = Tk()
# устанавливаем название окна
root.title("Калькулятор квадратных уравнений")
# устанавливаем минимальный размер окна
root.minsize(325, 230)
# выключаем возможность изменять окно
root.resizable(width=False, height=False)

# создаем рабочую область
frame = Frame(root)
frame.grid()

# поле для ввода первого аргумента уравнения (a)
a = Entry(frame, width=3)
a.bind("<FocusIn>", clear)
a.grid(row=1, column=1, padx=(10, 0))

# текст после первого аргумента
a_lab = Label(frame, text="x^2+").grid(row=1, column=2)

# поле для ввода второго аргумента уравнения (b)
b = Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1, column=3)
# текст после второго аргумента
b_lab = Label(frame, text="x + ").grid(row=1, column=4)

# поле для ввода третьего аргумента уравнения (с)
c = Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
# текст после третьего аргумента
c_lab = Label(frame, text="= 0 ").grid(row=1, column=6)

# кнопка решить

but = Button(frame, text="Решить", command=handler).grid(row=1, column=7, padx=(10, 0))

# место для вывода решения уравнения
output = Text(frame, bg="white", font="TimesNewRoman 16", width=35, height=14)
output.grid(row=2, columnspan=8)

# запускаем главное окно
root.mainloop()
