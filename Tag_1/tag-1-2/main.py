import arcade

# Öffne ein weißes Fenster
screen = arcade.get_screens()[0]
arcade.open_window(screen.width, screen.height, "Arcade")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

# Hier kannst du zeichnen
arcade.draw_xywh_rectangle_filled(50, 100, 100, 50, arcade.color.YELLOW)

arcade.finish_render()

# Startet das Programm
arcade.run()