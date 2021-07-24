import con_draw

win = con_draw.Drawer((30, 30), "#")
list_of_strings = [
    "*", "**", "***", "****"
]
frames_1 = con_draw.Frames(list_of_strings)

class frames_2(con_draw.BaseFramesClass):
    frames = list_of_strings

for frame in win.frames():
    frame.draw()
    frame.play_frame((1, 1), frames_1)
    frame.play_frame((1, 2), frames_2)
    frame.update()
