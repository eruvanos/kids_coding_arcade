import arcade

# Öffne ein weißes Fenster
width = arcade.get_screens()[0].width
height = arcade.get_screens()[0].height
window = arcade.open_window(width, height, "Arcade")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

# Hier kannst du zeichnen

# Der Boden
arcade.draw_lrtb_rectangle_filled(0, width, 100, 0, arcade.csscolor.GREEN)

# Ein Baum
arcade.draw_rectangle_filled(300, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(300, 300, 270, 220, 330, 220, arcade.csscolor.DARK_GREEN)

arcade.finish_render()

# Startet das Programm
arcade.run()