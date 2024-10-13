# обработчик изображений

from tkinter import *
from tkinter import filedialog  # файловый диалог
from PIL import Image, ImageTk


class App:  # класс нашего приложения
    def __init__(self):
        self.root = Tk()  # корневой элемент
        self.root.title('Обработка изображений')
        self.root.geometry('800x600')
        self.root.resizable(False, False)  # фиксируем габариты
        self.root.iconphoto(False, PhotoImage(file='icon.png'))
        self.label = Label(text='Работаем с картинками',
                           background='#ffff00',
                           foreground='red',
                           font=('Verdana', 16))
        self.label.pack()  # размещение надписи
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)
        self.btn = Button(text='Покажись', command=self.load)
        self.btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.rect_btn = Button(text='Прямоугольник', command=self.make_rect)
        self.rect_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        #self.btn.bind('<ButtonPress-1>', self.load)
        self.image = None
        self.empty = Image.new('RGB', (600, 400), (255, 255, 255))  # пустышка
        self.root.mainloop()

    def load(self):
        try:
            fullpath = filedialog.askopenfilename(initialdir='./',
                                                  filetypes=(
                                                      ('JPEG', '*.jpg'),
                                                      ('PNG', '*.png')
                                                  ))  # диалог открытия картинки
            self.empty = Image.open(fullpath)
            mode = self.empty.mode # получаем цветовую схему
            if mode == 'P': # 256- color indexed image
                self.empty = self.empty.convert('RGB')
            w,h = self.empty.size
            if w>600:
                ratio = w / 600
                self.empty = self.empty.resize((600, int(h/ratio)))
            else:
                pass
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        except AttributeError:  # если не удалось подгрузить
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    def make_rect(self):
        self.canvas.create_rectangle(0, 0, 600, 400, outline='#000000',
                                     fill='#80CBC4',
                                     width=5)


app = App()
