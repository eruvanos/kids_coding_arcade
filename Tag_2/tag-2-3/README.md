# Wir ändern ein wenig und benutzen die Maus


## Die Zeichenmethode

Um auch das Zeichnen wieder verwenden zu können, lohnt es sich, die Befehle in eine eigene Funktion zu tun.

```python
def draw():
    arcade.start_render()
    # Hier kannst du nun zeichnen
    
    baum(190, 190)
    
    arcade.finish_render()

draw()
```


## Figuren

Arcade bietet dir die Möglichkeit Figuren zu erstellen und auf dem Bildschirm zu bewegen.

```python
alien = arcade.Sprite(arcade.resources.image_alien_blue_front)
biene = arcade.Sprite(arcade.resources.image_bee)
spielerin = arcade.Sprite(arcade.resources.image_female_adventurer_idle)
spieler = Sprite(arcade.resources.image_male_adventurer_idle)
```

Es gibt noch viel mehr Figuren und Bilder, die ihr benutzen könnt. Schaut mal [hier](http://arcade-gui.s3-website.eu-central-1.amazonaws.com/resources.html#resources-images-alien).

## Die Maus benutzen

Es gibt die möglichkeit, dass ihr mit der Maus dinge bewegt oder anderes tut. Hier ist ein Beispiel:

```python
alien = arcade.Sprite(arcade.resources.image_alien_blue_front)

@window.event("on_mouse_motion")
def wenn_maus_bewegt(x, y, button, modifier):
    alien.center_x = x
    alien.center_y = y

    # Fehlt hier noch was?
```

> Übernehmt die Mausfunktion und verschiebt eure Figur.


