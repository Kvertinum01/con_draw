from typing import List


class BaseFramesClass:
    """
    Класс для использования списков
    (Функция play_frame в основном классе)
    """

    frames = []
    nowframe = 0

    @classmethod
    def _get_frame(cls):
        frame = cls.frames[cls.nowframe]
        cls.nowframe = cls.nowframe + 1 \
            if cls.nowframe + 1 < len(cls.frames) \
                else 0
        return frame


class Frames(BaseFramesClass):
    """
    Класс для удобного использования BaseFramesClass
    """
    
    @classmethod
    def __init__(cls, frames: List[str]) -> None:
        cls.frames = frames
