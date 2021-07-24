import con_draw

win = con_draw.Drawer((80, 80), "#") #Создаем холст
image = con_draw.Image("mushroom.png") #Загружаем картинку
str_image = image.load((80, 80)) #Получаем картинку в формате str

for frame in win.frames():
    frame.draw()
    frame.add_big_str(
        (1, 1), str_image
    ) #Рисуем картинку на весь холст
    frame.update()
