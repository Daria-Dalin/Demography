# Доп библиотека PIL (pillow)
from PIL import ImageDraw, Image
from PIL.ImageFont import ImageFont

# создаем и рисуем
# 1 холст
canvas = Image.new('RGB', (200, 200), (255, 255, 255))

# создаем рисовальщик
draw = ImageDraw.Draw(canvas)
# рисуем линию Окна
draw.line((100, 0, 200, 200), fill='brown', width=3)
draw.line((0, 100, 200, 100), fill='brown', width=3)
# рисуем многоугольник
draw.rectangle((0, 0, 50, 50), outline=(0, 250, 250), width=5)
# напишем текст
text = 'окно'

draw.text((80, 90), text, )
# рисуем полигон(треугольник)
draw.polygon(
    xy=(
        (200, 200)
        (150, 250)
        (200, 150)
    ), fill='red', outline=(0, 0, 0)
)
# рисуем круг
draw.ellipse((0,0,200,200), outline='brown', width=5)
# сохраняем
canvas.save('line.png', 'PNG')
