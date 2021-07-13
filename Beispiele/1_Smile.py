import arcade

# Dies sind Variablen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Happy Face Example"

# Öffne ein Fenster
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Setze die Hintergrundfarbe auf weiß
arcade.set_background_color(arcade.color.WHITE)

# Starte das zeichnen
arcade.start_render()

# --- Hier kommen die Befehle, um zu Zeichnen ---

# Zeichne das Gesicht
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Zeichne das rechte Auge
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Zeichne das linke Auge
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Zeichne das Lächeln
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle,
                        end_angle, 10)

# Beende das Zeichnen und zeige das Bild
arcade.finish_render()

# Zeige das Fenster
arcade.run()
