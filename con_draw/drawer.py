from .frame import Frame
from typing import (
    List,
    Union,
    Tuple,
    Generator
)
import time


class Drawer:
    """Основные настройки и генератор фреймов"""
    
    def __init__(
        self, 
        winsize: Union[List[int], Tuple[int]],
        char: str = " ",
        auto_correct = True
    ) -> None:
        self.drawing = True
        self.winsize = list(winsize)
        if auto_correct:
            self.winsize[1] = self.winsize[1] // 2
        self.char = char

    def frames(self, pause=.4) -> Generator[Frame, None, None]:
        while self.drawing:
            try:
                yield Frame(self)
                time.sleep(pause)
            except KeyboardInterrupt:
                break
