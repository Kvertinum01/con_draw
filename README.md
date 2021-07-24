<h1 align="center">
  con_draw (0.x)
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/made%20by-Kvertinum01-green">
</p>

> Простейший фреймворк для рисования в консоли

## Hello World
```python
import con_draw

win = con_draw.Drawer((30, 30), "#") #(30, 30) - размер холста, "#" - чем холст будет заполнен

for frame in win.frames():
    frame.draw()
    frame.add_str((3, 5), "Hello world") # (3, 5) - координаты x и y
    frame.update()
```

#### Больше примеров [здесь](/docs)

## Установка
### Новейшая версия
```shell
pip install -U "git+https://github.com/Kvertinum01/con_draw#egg=con_draw"
```