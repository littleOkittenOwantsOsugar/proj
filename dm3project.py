from tkinter import *
import copy
from matplotlib import pyplot as plt
import math
import numpy as np


def test():
    user_input=txt.get()
    answer(user_input)

def answer(user_input):
    if user_input == 'граф':
        root.destroy()
        import dm3project2.py
    elif user_input == 'орграф':
        root.destroy()
        import dm3project1.py


root = Tk()
root.title('DM 3 TASK')
root.geometry('600x600')
root.configure(bg='#FFAAAA')
lbl = Label(root, text="Напишите `граф` или `орграф`:")
lbl.grid(column=0, row=0)
txt = Entry(root, width=10)
txt.grid(column=1, row=0)
btn = Button(root,  # родительское окно
             text="Click me",  # надпись на кнопке
             width=30, height=5,  # ширина и высота
             bg="white", fg="black",
             command=test)
btn.grid(column=2, row=0)

root.mainloop()

