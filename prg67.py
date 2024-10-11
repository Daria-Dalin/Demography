# Доп библиотека PIL (pillow)
from PIL import Image, ImageFilter, ImageDraw

# пробуем прочитать файл original.jpg
try:
    orig = Image.open('original.jpg')
except FileNotFoundError:
    print('Файл не найден')

print('Параметры счтано файла:')
print(f'формат: {orig.format}')
print(f'размеры: {orig.size}')
print(f'цветовая схема: {orig.mode}')

w, h = orig.size  # получили и распаковали кортеж
pixels = orig.load()  # список пикселей [х y]


for x in range(w):
    for y in range(h):
        r, g, b = pixels[x, y]
        average = (r + g + b) // 3
        pixels[x, y] = average, average, average

orig.save('grayscale.jpg')

blur = orig.filter(ImageFilter.BLUR)
cropped = orig.crop((200, 0, 400, 260))
contour = orig.filter(ImageFilter.CONTOUR)
cropped.save('cropped.jpg')
blur.save('blur.jpg')
contour.save('contour.jpg')
