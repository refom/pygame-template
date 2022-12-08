
from scripts.window import Window
from scripts.camera import Camera

window = Window()
camera = Camera()

while True:
    camera.update()
    camera.custom_draw(window.display)

    window.input()
    window.draw()


