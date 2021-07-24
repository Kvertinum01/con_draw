from typing import Tuple, Optional


class Image:
    """
    Класс для преобразования обычного изображания в ASCII символы
    """
    
    def __init__(self, path: str, chars: str = "@1#$% &*()ab"):
        from PIL import Image
        self.image = Image.open(path)
        self.chars = list(chars)
        self.auto_correct = True

    def load(self, resize: Optional[Tuple[int, int]]=None):
        if resize is None:
            resize = self.image.size
        else:
            resize = (resize[0], resize[1] // 2) \
                if self.auto_correct else resize
        width, height = resize
        image = self.image.resize((width, height))
        image = image.convert("L")
        pix = image.getdata()
        pixels = [self.chars[char//25] for char in pix]
        str_image = ""
        for h in range(height):
            str_image += "".join(
                pixels[width*(h-1):width*h]
            ) + "\n"
        return str_image
