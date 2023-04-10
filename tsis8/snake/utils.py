from pygame import image
from os import sep

# Images
_image_library = {}
def get_image(path):
        global _image_library
        img = _image_library.get(path)
        if img == None:
                canonicalized_path = path.replace('/', sep).replace('\\', sep)
                img = image.load(canonicalized_path)
                _image_library[path] = img
        return img


def checkInSnake(parts, radius = 15, x = -1, y = -1):
        for p_x, p_y in parts:
                if x != -1:
                        if p_x - radius < x and x < p_x + radius:
                                return True
                if y != -1:
                        if p_y - radius < y and y < p_y + radius:
                                return True
        return False
