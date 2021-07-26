from random import randint

import arcade
# Öffne ein weißes Fenster
from arcade import SpriteCircle

screen = arcade.get_screens()[0]
width = screen.width
height = screen.height - 50
window = arcade.open_window(width, height, "Arcade")
arcade.set_background_color(arcade.color.WHITE)

@window.event
def on_key_press(symbol, modifier):
    # Hier wird Code ausgeführt, wenn eine Taste gedrückt wird
    ...


@window.event
def on_key_release(symbol, modifier):
    # Hier wird Code ausgeführt, wenn eine Taste losgelassen
    ...

@window.event
def on_draw():
    arcade.start_render()

    # Hier kannst du zeichnen


def update(dt):
    # Dies wird circa 60 mal in der Sekunde ausgeführt
    ...


@window.event
def on_mouse_press(x, y, button, modifier):
    # Dies wird ausgeführt, wenn die Maus gedrückt wird
    ...


# Startet das Programm
arcade.schedule(update, 1 / 60)
arcade.run()
