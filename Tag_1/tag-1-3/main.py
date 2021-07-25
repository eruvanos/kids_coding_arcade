import arcade

# Öffne ein weißes Fenster
width = arcade.get_screens()[0].width
height = arcade.get_screens()[0].height
window = arcade.open_window(width, height, "Arcade")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

# Hier kannst du zeichnen

# Der Boden
arcade.draw_xywh_rectangle_filled(0, 0, width, 100, arcade.csscolor.GREEN)

# Ein Baum
x = 290
y = 190
# Baumstamm
arcade.draw_xywh_rectangle_filled(x, y, 20, 60, arcade.csscolor.SIENNA)
# Baumkrone
arcade.draw_triangle_filled(x-20, y+30, x+10, y+110, x+40, y+30, arcade.csscolor.DARK_GREEN)
# Roter Punkt
arcade.draw_circle_filled(x,y, 3, arcade.color.RED)

arcade.finish_render()

# Startet das Programm
arcade.run()