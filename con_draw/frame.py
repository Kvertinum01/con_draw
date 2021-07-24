import sys
import os
from typing import List, Tuple, Union
from .other import Frames


class Frame:
    def __init__(self, window) -> None:
        self.window = window
        self._bg = [
            window.char * window.winsize[0] for _ in range(window.winsize[1])
        ]
        self.result: List[str] = []

    def draw(self) -> List[str]:
        """
        Изменение холста на прямоугольник с заданными заранее значениями
        """
        
        self.result = self._bg
        return self.result

    def add_str(
        self, 
        position: Union[List[int], Tuple[int]], 
        string: str
    ) -> List[str]:
        """
        Изменение символов на холсте по x и y
        """

        line = self.result[position[1]-1]
        line_start = line[:position[0]-1]
        line_end = line[len(string)+position[0]-1:]
        self.result[position[1]-2] = line_start + string + line_end
        return self.result

    def add_big_str(
        self,
        position: Union[List[int], Tuple[int]], 
        string: str
    ) -> List[str]:
        """
        Изменения символов по x и y с возможностью использовать "\n"
        """

        strings = string.split("\n")
        lines = self.result[position[0]-1:position[0]-1+len(strings)]
        for ind, line in enumerate(lines):
            string = strings[ind]
            line_start = line[:position[0]-1]
            line_end = line[len(string)+position[0]-1:]
            self.result[position[1]-2+ind] = line_start + string + line_end
        return self.result

    def add_list(
        self,
        position: Union[List[int], Tuple[int]],
        strings_list: List[str]
    ) -> List[str]:
        """
        Изменение символов по x и y
        Вместо строки на вход идет список
        Каждый элемент списка начинается с новой строки
        """

        return self.add_big_str(
            position, "\n".join(strings_list)
        )

    def draw_line(
        self,
        pos_one: Union[List[int], Tuple[int]],
        pos_two: Union[List[int], Tuple[int]],
        char: str
    ) -> List[str]:
        """Рисование линии от 1 точки до 2"""

        x1, y1, x2, y2 = pos_one + pos_two
        delta_x = abs(x2-x1)
        delta_y = abs(y2-y1)
        error = 0
        delta_err = (delta_y + 1) / (delta_x + 1)
        y = y1
        dir_y = y2-y1
        dir_y = 1 if dir_y > 0 else -1
        for x in range(x1, x2+1):
            self.add_str((x, y), char)
            error += delta_err
            if error >= 1.0:
                y += dir_y
                error -= 1
        return self.result

    def draw_circle(
        self,
        center_position: Union[List[int], Tuple[int]],
        radius: int,
        char: str
    ) -> List[str]:
        """Рисование круга"""

        disp_x, disp_y = center_position
        x, y = 0, radius
        delta = (1 - 2 * radius)
        error = 0
        while y >= 0:
            self.add_str((disp_x + x, disp_y + y), char)
            self.add_str((disp_x + x, disp_y - y), char)
            self.add_str((disp_x - x, disp_y + y), char)
            self.add_str((disp_x - x, disp_y - y), char)
            error = 2 * (delta + y) - 1
            if delta < 0 and error <=0:
                x += 1
                delta += 2 * x + 1
                continue
            error = 2 * (delta - x) - 1
            if delta > 0 and error > 0:
                y -= 1
                delta += 1 - 2 * y
                continue
            x += 1
            delta = delta + 2 * (x - y) 
            y -= 1
        return self.result

    def play_frame(
        self,
        position: Union[List[int], Tuple[int]],
        frames: Frames
    ) -> List[str]:
        """
        Проход по списку
        Каждый фрейм - следующий элемент из списка
        """

        frame = frames._get_frame()
        self.add_big_str(position, frame)
        return self.result

    def update(self) -> None:
        """Очищение консоли и рисование нового фрейма"""

        os.system("cls || clear")
        sys.stdout.write(
            "\n".join(self.result)
        )
        self.result = []
