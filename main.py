
from scripts.window import Window

class Game:
    def __init__(self):
        self.window = Window()

    def update(self):
        # anything on top
        self.window.input()
        self.window.render()

    def run(self):
        while True:
            self.update()

Game().run()
