# Spickzettel

Beim Programmieren schreibt man Text, und gibt dem Computer Befehle.

## Starte hier

```python
import arcade

# Öffne ein weißes Fenster
width = arcade.get_screens()[0].width
height = arcade.get_screens()[0].height
window = arcade.open_window(width, height, "Arcade")
arcade.set_background_color(arcade.color.CHROME_YELLOW)

arcade.start_render()

# Hier kannst du zeichnen

arcade.finish_render()

# Startet das Programm
arcade.run()
```

## For-Schleifen

```python
for x in range(10):
    # Dies zeichnet 10 Bäume, im Abstand von 50 Pixel
    baum(x * 50, 190)
```

## Funktionen

```python
# Eine Funktion fängt an mit 'def', einem Namen und den Klammern
def baum(x, y):  # In den Klammern könnt ihr angeben, welche informationen ihr braucht 
    # alle Befehle, die ausgeführt werden sollen, müssen eingerückt werden:
    arcade.draw_xywh_rectangle_filled(x, y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x - 20, y + 30, x + 10, y + 110, x + 40, y + 30, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(x, y, 3, arcade.color.RED)


baum(290, 190)
```

## Zeichenbefehle

```python
import arcade

# Linie
arcade.draw_line(0, 0, 50, 50, arcade.color.YELLOW)

# Rechteck
arcade.draw_xywh_rectangle_filled(150, 100, 100, 50, arcade.color.YELLOW)
arcade.draw_xywh_rectangle_outline(150, 100, 100, 50, arcade.color.YELLOW)

# Kreis
arcade.draw_circle_filled(50, 100, 10, arcade.color.YELLOW)
arcade.draw_circle_outline(50, 100, 10, arcade.color.YELLOW)
```

## Farben

| Farbe      | Code                  |
| -------    | -------------------   |
| gelb       | arcade.color.YELLOW   |
| rot        | arcade.color.RED      |
| grün       | arcade.color.GREEN    |
| blau       | arcade.color.BLUE     |
| himmelblau | arcade.color.SKY_BLUE |
| weiß       | arcade.color.WHITE    |
| schwarz    | arcade.color.BLACK    |

[Noch mehr Farben](http://arcade-gui.s3-website.eu-central-1.amazonaws.com/arcade.color.html)

### Beispiel - Zufällige Farbe

```python
import arcade
from random import choice

farben = [
    arcade.color.YELLOW,
    arcade.color.RED,
    arcade.color.GREEN,
    arcade.color.BLUE,
    arcade.color.WHITE,
    arcade.color.BLACK
]

arcade.draw_circle_filled(50, 100, 10, choice(farben))
```

## Koordinaten System

Um einen Punkt auf dem Bildschirm anzugeben müsst ihr zwei Zahlen angeben X und Y.

X - Gibt an wie weit von links nach rechts Y - Gibt an wie viel von unten nach oben

![](./koordinaten.png)

