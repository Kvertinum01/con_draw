# Frame
Класс для рисования в консоли <br/>
Расположение: con_draw.frame

## Пример [здесь](/con_draw/drawer.py)

## draw()
Изменение холста на прямоугольник с заданными заранее значениями

## add_str(position, string)
По координатам x и y добавляет строку

## add_big_str(position, string)
По координатам x и y добавляет строку. Можно использовать \n

## draw_line(pos_one, pos_two, char)
Рисует линию от pos_one к pos_two символом char

## draw_circle(center_position, radius, char)
Рисует круг, центр которого - center_position, а радиус - radius

## play_frame(position, frames)
Функция для использования класса `Frames`

## update()
Очищение консоли и рисование нового фрейма
