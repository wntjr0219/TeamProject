from pico2d import *

class Grass:
    image = None
    def __init__(self):
        if Grass.image == None:
            self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
