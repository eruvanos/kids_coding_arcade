# Spickzettel

Beim Programmieren schreibt man Text, und gibt dem Computer Befehle.

## Starte hier

```python
import arcade

# Öffne ein Fenster
width = arcade.get_screens()[0].width
height = arcade.get_screens()[0].height
window = arcade.open_window(width, height, "Arcade")
window.set_mouse_visible(False)
arcade.set_background_color(arcade.color.CHROME_YELLOW)

# So erstellt man eine Spielerin oder einen Spieler
figur = arcade.Sprite(arcade.resources.image_alien_blue_front)
# figur = arcade.Sprite(arcade.resources.image_bee)
# figur = arcade.Sprite(arcade.resources.image_female_adventurer_idle)
# figur = Sprite(arcade.resources.image_male_adventurer_idle)

# So kann man einen SpielerIn positionieren
figur.center_x = 100
figur.center_y = 100

# Hier Zeichnen wir
def draw():
    arcade.start_render()
    # Hier kann man noch mehr zeichnen, zum Beispiel einen Wald
    figur.draw()
    arcade.finish_render()

draw()
arcade.run()

```


## Auf die Maus reagieren

```python
# Nun wird es nochmal richtig spannend: wir benutzen die Maus, um den Spieler zu bewegen
@window.event("on_mouse_motion")
def wenn_maus_bewegt(x, y, button, modifier):
    pass
```

## Erstelle eine Figur
```python
import arcade

alien = arcade.Sprite(arcade.resources.image_alien_blue_front, scale=0.8)

# Hiermit kann man eine Figur auf dem Bildschirm positionieren
alien.center_x = 100
alien.center_y = 200

# Hiermit kann man eine Figur zeichnen
alien.draw()
```

Natürlich gibt es noch viel mehr Figuren, die du benutzen kannst, schau doch mal hier:
[Übersicht](http://arcade-gui.s3-website.eu-central-1.amazonaws.com/resources.html)

## Eine Zeichenfunktion

Um auch das Zeichnen wieder verwenden zu können, lohnt es sich, die Befehle in eine eigene Funktion zu tun.

```python
def draw():
    arcade.start_render()
    # Hier kannst du nun zeichnen
    arcade.finish_render()
```

## For-Schleifen

```python
for x in range(10):
    # Dies zeichnet 10 Bäume, im abstand von 50 Pixel
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

