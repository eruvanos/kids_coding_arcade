import arcade

# Öffne ein Fenster
width = arcade.get_screens()[0].width
height = arcade.get_screens()[0].height
window = arcade.open_window(width, height, "Sternensammler")
window.set_mouse_visible(False)
arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

# Die Spielfigur
alien = arcade.Sprite(arcade.resources.image_alien_blue_walk2, scale=0.5)
alien.center_x = 100
alien.center_y = 100

# Punkte
punkte = 0

# Sterne
sterne = arcade.SpriteList()

# TODO Hier fehlen uns Sterne, erstelle bitte ein paar Sterne über dem Wald im Himmel


# Hintergrund
def mond(x, y):
    arcade.draw_circle_filled(x, y, 100, arcade.color.GHOST_WHITE)

def boden():
    arcade.draw_xywh_rectangle_filled(0, 0, width, 150, arcade.color.DARK_GREEN)

def baum(x, y):
    arcade.draw_xywh_rectangle_filled(x, y, 20, 60, arcade.color.SIENNA)
    arcade.draw_triangle_filled(x - 20, y + 30, x + 10, y + 110, x + 40, y + 30, arcade.color.CHARLESTON_GREEN)
    # Den roten Punkt brauchen wir nicht mehr, wir wissen ja wo die Bäume sind ;)
    # arcade.draw_circle_filled(x, y, 3, arcade.color.RED)

def wald():
    mond(550, 450)
    boden()
    for x in range(5):
        baum(190 + 100 * x, 100)


# Zeichenfunktion
def draw():
    arcade.start_render()
    wald()
    alien.draw()

    # TODO Hier müssen die Sterne gezeichnet werden


    # NEU Hier zeigen wir den Punktestand an
    arcade.draw_text(f"Du hast {punkte} Punkte", 10, 50, arcade.color.WHITE)
    arcade.finish_render()


# Diese Funktion wird ausgeführt, wenn die Maus bewegt wird
@window.event("on_mouse_motion")
def wenn_maus_bewegt(x, y, dx, dy):
    global punkte  # dies brauchen wir um den Punktestand zu ändern
    alien.center_x = x
    alien.center_y = y

    # TODO Alle Sterne nach unten bewegen


    # TODO Hier sollten wir schauen, ob das Alien einen Stern berührt und diesen dann entfernen
    # du kannst dann auch die Punkte ändern mit:
    # punkte = punkte + 10

    draw()


draw()
arcade.run()
