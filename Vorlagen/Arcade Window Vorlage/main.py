"""
Dein erstes Spiel
"""
import arcade


class MeinSpiel(arcade.Window):
    def __init__(self):
        # Dies stellt die Fenstergröße auf die Bildschirmgröße
        screen = arcade.get_screens()[0]
        super().__init__(screen.width, screen.height, "Mein Spiel")

        # Setze die Hintergrund Farbe auf ein hellblau
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        # Hier kannst du Bilder Laden oder anderes tun, was nur einmal
        # beim Starten deines Spiels passieren muss
        pass

    def on_draw(self):
        # Hier zeichnen wir das Spiel, wichtig ist es dem Computer zu sagen,
        # dass wir anfangen wollen zu Zeichnen
        arcade.start_render()

        # Hier müssen deine Befehle zum Zeichnen hin
        arcade.draw_line(0, 0, 50, 50, arcade.color.YELLOW)


def main():
    # Erstelle dein Spiel
    window = MeinSpiel()

    # Bereite es vor
    window.setup()

    # Starte es
    arcade.run()

# Dies wird benötigt, um das Spiel zu starten
if __name__ == "__main__":
    main()
