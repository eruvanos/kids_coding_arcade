from random import randint

import arcade
# Öffne ein weißes Fenster
from arcade import SpriteCircle

screen = arcade.get_screens()[0]
width = screen.width
height = screen.height - 50
window = arcade.open_window(width, height, "Arcade")
arcade.set_background_color(arcade.color.WHITE)


computer = arcade.load_texture(arcade.resources.image_bee)
computer_x = 50
computer_y = 300

player = arcade.load_texture(arcade.resources.image_female_adventurer_idle)
player_x = 50
player_y = 100

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
    arcade.draw_texture_rectangle(player_x, player_y, player.width, player.height, player)
    arcade.draw_texture_rectangle(computer_x, computer_y, computer.width, computer.height, computer)


def update(dt):
    # Dies wird circa 60 mal in der Sekunde ausgeführt
    global computer_x
    computer_x += randint(2,10) * dt


@window.event
def on_mouse_press(x, y, button, modifier):
    # Dies wird ausgeführt, wenn die Maus gedrückt wird
    global player_x
    player_x += 10


# Startet das Programm
arcade.schedule(update, 1 / 60)
arcade.run()
