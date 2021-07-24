import con_draw

win = con_draw.Drawer((50, 50), "#")

for frame in win.frames():
    frame.draw()
    frame.draw_line((1, 1), (5, 5), "*")
    frame.draw_circle((10, 10), 4, "@")
    frame.update()
