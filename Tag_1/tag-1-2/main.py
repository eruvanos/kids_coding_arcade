import arcade

# Öffne ein weißes Fenster
screen = arcade.get_screens()[0]
window = arcade.open_window(screen.width, screen.height, "Arcade")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

# Hier kannst du zeichnen
arcade.draw_lrtb_rectangle_filled(0, screen.width, screen.height/2, 0, arcade.csscolor.GREEN)

arcade.finish_render()

arcade.run()