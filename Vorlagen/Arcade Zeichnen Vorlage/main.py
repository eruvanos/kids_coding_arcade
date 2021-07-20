import arcade

# Öffne ein weißes Fenster
screen = arcade.get_screens()[0]
arcade.open_window(screen.width, screen.height, "Arcade")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# Hier kannst du zeichnen

arcade.finish_render()

# Startet das Programm
arcade.run()