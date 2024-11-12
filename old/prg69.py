# GUI - graphic user interface
# PyQt6
import tkinter
from tkinter import mainloop

from PIL import Image, ImageTk

class App:
    def __init__(self):

        # корневой элемент приложения
        self.root = tkinter.Tk()

        # рабочая областиь
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        # добавляем ярлык
        self.label = tkinter.Label(self.frame, text='GUI').grid(row=1, column=1)



        # добавим кнопку
        self.but = tkinter.Button(frame,
                             text='заменить',
                             command=change).grid(row=2, column=1)

        # добавим холст
        self.c = tkinter.Canvas(self.root, height=400, width=600)
        self.image = Image.open('original.jpg')
        self.photo = ImageTk.PhotoImage(image)
        self.image = c.create_image(0, 0, anchor='nw', image=photo)
        c.grid(row=2, column=1)
    def change():
        print('кнопка нажата')
        self.image = Image.open('inverted.jpg')
        self.photo = ImageTk.PhotoImage(image)
        self.image = c.create_image(0, 0, anchor='nw', image=photo)
        self.c.grid(row=2, column=1)

app= App()
