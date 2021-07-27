import arcade

# Öffne ein weißes Fenster
width = arcade.get_screens()[0].width
height = arcade.get_screens()[0].height
window = arcade.open_window(width, height, "Arcade")
arcade.set_background_color(arcade.color.CHROME_YELLOW)
arcade.start_render()


# Sonne
def sonne(x, y):
    arcade.draw_circle_filled(x, y, 100, arcade.color.CADMIUM_YELLOW)


# Der Boden
def boden():
    arcade.draw_xywh_rectangle_filled(0, 0, width, 150, arcade.csscolor.GREEN)


def baum(x, y):
    arcade.draw_xywh_rectangle_filled(x, y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x - 20, y + 30, x + 10, y + 110, x + 40, y + 30, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(x, y, 3, arcade.color.RED)


# Hier wird die erste Funktion benutzt
sonne(190, 100)

boden()

# Ein Baum
# > Hier musst du ein For Schleife benutzen
baum(190, 120)
baum(240, 120)
baum(290, 120)
baum(340, 120)
baum(390, 120)
baum(440, 120)
baum(490, 120)

# Startet das Programm
arcade.finish_render()
arcade.run()
