import arcade

# Öffne ein weißes Fenster
from arcade import Sprite

width = arcade.get_screens()[0].width
height = arcade.get_screens()[0].height
window = arcade.open_window(width, height, "Arcade")
window.set_mouse_visible(False)
arcade.set_background_color(arcade.color.CHROME_YELLOW)

# Hier kommt was neues:

# So erstellt man eine Spielerin oder einen Spieler
alien = arcade.Sprite(arcade.resources.image_alien_blue_front, scale=0.5)

# Ein Sprite ist sowas wie eine Figur, die man über den Bildschirm bewegen kann.
# Dafür kannst du die x und y Werte so setzen:
alien.center_x = 100
alien.center_y = 100

# Dies solltet ihr schon kennen, dies sind Funktionen für den Wald
def sonne(x, y):
    arcade.draw_circle_filled(x, y, 100, arcade.color.CADMIUM_YELLOW)


def boden():
    arcade.draw_xywh_rectangle_filled(0, 0, width, 150, arcade.csscolor.GREEN)


def baum(x, y):
    arcade.draw_xywh_rectangle_filled(x, y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x - 20, y + 30, x + 10, y + 110, x + 40, y + 30, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(x, y, 3, arcade.color.RED)


def wald():
    sonne(190, 100)
    boden()
    for x in range(5):
        baum(190 + 50 * x, 100)

# Das ist NEU: auch unsere Zeichenfunktionen kommen in eine Funktion
def draw():
    arcade.start_render()
    wald()
    alien.draw()
    arcade.finish_render()

# Aufgabe: Nun sollten wir etwas mit der Maus machen

draw()
arcade.run()
