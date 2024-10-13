# обработчик изображений
import tkinter
from re import fullmatch
from tkinter import *
from tkinter import filedialog  # файловый диалог
from PIL import Image, ImageTk, ImageFilter, ImageEnhance


class App:  # класс нашего приложения
    def __init__(self):  # конструктор
        self.root = Tk()  # корневой элемент
        self.root.title('Обработка изображений')
        self.root.geometry('800x600')
        self.root.resizable(False, False)  # фиксируем габариты
        self.root.iconphoto(False, PhotoImage(file='images/logo.png'))
        self.label = Label(text='Работаем с картинками',
                           background='#ffff00',
                           foreground='red',
                           font=('Verdana', 16))
        self.label.pack()  # размещение надписи
        self.canvas = Canvas(bg='white', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)
        photo = PhotoImage(file='logo.png')
        # Кнопка загрузки
        self.btn = Button(text='Загрузить',
                          bg='yellow', fg='purple', activebackground='blue',
                          activeforeground='black',
                          image=photo, compound=BOTTOM,
                          borderwidth=3, relief="raised",
                          command=self.load)
        self.btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # кнопка размытия
        self.blur = Button(text='Размыть', bg='yellow', fg='purple',
                           borderwidth=3, relief="ridge",
                           image=photo, compound=BOTTOM,
                           activebackground='blue', activeforeground='black',
                           command=self.blur)
        self.blur.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # кнопка резкости

        self.shrp = Button(text='Резкость', bg='yellow', fg='purple',
                           borderwidth=3, relief="solid",
                           image=photo, compound = BOTTOM,
                           activebackground='blue', activeforeground='black',
                           command=self.sharp)
        self.shrp.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # кнопка отражения по горизонтали
        self.flp = Button(text='Отразить', bg='yellow', fg='purple',
                          borderwidth=3, relief="groove",
                          image=photo, compound=BOTTOM,
                          activebackground='blue', activeforeground='black',
                          command=self.flip)
        self.flp.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # кнопка вызова оригинал
        self.orig = Button(text='Оригинал', bg='yellow', fg='purple',
                           borderwidth=3, relief="ridge",
                           image=photo, compound=BOTTOM,
                           activebackground='blue', activeforeground='black',
                           command=self.back)
        self.orig.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # кнопка очистки
        self.rect_btn = Button(text='Очистить', bg='yellow', fg='purple',
                               borderwidth=3, relief="solid",
                               image=photo, compound=BOTTOM,
                               activebackground='blue', activeforeground='black',
                               command=self.make_rect)
        self.rect_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        # кнопка Сохранить
        self.save_btn = Button(text='Сохранить', bg='yellow', fg='purple',
                               borderwidth=3, relief="groove",
                               image=photo, compound=BOTTOM,
                               activebackground='blue', activeforeground='black',
                               command=lambda: self.load_save('save'))
        self.save_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.save_btn['state'] = DISABLED
        # self.btn.bind('<ButtonPress-1>', self.load)
        self.left, self.top = 0, 0  # точки привязки к холсту
        self.ext = ''  # расширение файла картинки
        self.image = None

        self.empty = Image.new('RGB', (600, 400), (255, 255, 255))  # пустышка
        self.root.mainloop()


    def load(self):
        try:
            fullpath = filedialog.askopenfilename(initialdir='./',
                                                  filetypes=(
                                                      ('ALL', '*.*'),
                                                      ('JPEG', '*.jpg'),
                                                      ('PNG', '*.png')
                                                  ))  # диалог открытия картинки
            self.ext = fullpath.split('.')[-1]  # получаем расширение
            # print(self.ext)
            self.empty = Image.open(fullpath)
            mode = self.empty.mode  # получаем цветовую схему
            if mode == 'P':  # 256- color indexed image
                self.empty = self.empty.convert('RGB')
            w, h = self.empty.size

            if w > 600:
                ratio = w / 600
                h = int(h / ratio)
                w = 600
                self.empty = self.empty.resize((w, h))
                if h < 400:
                    self.left, self.top = 0, (400 - h) // 2
                else:
                    self.left, self.top = 0, 0
            else:
                self.left = (600 - w) // 2
                self.top = (400 - h) // 2

            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        except AttributeError:  # если не удалось подгрузить
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)

    # функционал кнопки размыть
    def blur(self):
        blur_img = self.empty.filter(ImageFilter.GaussianBlur(5))
        self.image = ImageTk.PhotoImage(blur_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL
        # функционал кнопки Резкость

    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.empty)
        sharp_img = sharper.enhance(5.0)
        self.image = ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = NORMAL

    # Функционал кнопки Отразить
    def flip(self):
        flp_img = self.empty.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.image = ImageTk.PhotoImage(flp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)

    # Функционал кнопки возврата к оригиналу
    def back(self):
        self.image = ImageTk.PhotoImage(self.empty)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        self.save_btn['state'] = DISABLED

    def load_save(self, *args):
        if len(args) == 1 and args[0] == 'save':
            fullpath = filedialog.asksaveasfilename(initialfile=f'result.{self.ext}')
            if fullpath != '':
                if f'.{self.ext}' not in fullpath:
                    fullpath += f'.{self.ext}'
                res = ImageTk.getimage(self.image)
                if res.mode == 'RGBA' and 'jp' in self.ext:
                    res = res.convert('RGB')
                res.save(fullpath)
                self.save_btn['state'] = DISABLED

    # код кнопки очистить
    def make_rect(self):
        self.canvas.create_rectangle(0, 0, 600, 400, fill='#ffffff')


app = App()
