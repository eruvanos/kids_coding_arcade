from random import randint

import arcade
# Öffne ein weißes Fenster
from arcade import SpriteCircle

screen = arcade.get_screens()[0]
width = screen.width
height = screen.height - 50
window = arcade.open_window(width, height, "Arcade")
arcade.set_background_color(arcade.color.WHITE)

bubbles = arcade.SpriteList()
score = 0
keys = set()

for _ in range(20):
    bubble = SpriteCircle(randint(10, 50), arcade.color.BLUE)
    bubble.center_x = randint(0, width)
    bubble.center_y = randint(-50, 0)
    bubble.change_y = randint(40, 70)
    bubbles.append(bubble)

@window.event
def on_key_press(symbol, modifier):
    keys.add(symbol)


@window.event
def on_key_release(symbol, modifier):
    keys.remove(symbol)

@window.event
def on_draw():
    arcade.start_render()
    bubbles.draw()

    arcade.draw_text(f"Score: {score}", 20, 20, color=arcade.color.BLACK, font_size=20)


def update(dt):
    global bubbles
    for bubble in bubbles:
        bubble.center_y += bubble.change_y * dt

    if arcade.key.SPACE in keys:
        bubbles = arcade.SpriteList()




@window.event
def on_mouse_press(x, y, button, modifier):
    global score
    getroffene_bubbles = arcade.get_sprites_at_point((x, y), bubbles)

    for bubble in getroffene_bubbles:
        bubble.center_x = randint(0, width)
        bubble.center_y = randint(-50, 0)
        score += 10


# Startet das Programm
arcade.schedule(update, 1 / 60)
arcade.run()
