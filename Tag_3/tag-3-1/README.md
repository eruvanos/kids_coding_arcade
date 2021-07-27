
## Viele Sterne / Listen

```python
# Dies erstellt eine neue Liste für Münzen
import arcade

sterne = arcade.SpriteList()

# Erstelle einen Stern
stern = arcade.Sprite(arcade.resources.image_star)
stern.center_x = 100
stern.center_y = 400

# Füge den Stern einer Liste hinzu
sterne.append(stern)

# Um alle Sterne zu bewegen, kannst du folgenden Befehl benutzen
# Hier werden alle Sterne 0 zur Seite bewegt und -2 nach unten
sterne.move(0, -2) 

def draw():
    arcade.start_render()
    # Dies zeichnet alle Sterne aus der Liste
    sterne.draw()
    arcade.finish_render()

```

### Entferne einen Stern

```python
# Dies entfernt einen Stern aus allen Listen
stern.remove_from_sprite_lists()
```

### Zusammenstoßen mit einem Stern

In Spielen möchte man oft schauen, ob die Spielfigur etwas berührt.
Dafür kann man folgendes benutzen:

```python
import arcade

# Die Spielfigur
alien = arcade.Sprite(arcade.resources.image_alien_blue_front, scale=0.8)
alien.center_x = 100
alien.center_y = 200

# Die Liste mit Sternen
sterne = arcade.SpriteList()

# Der erste Stern
stern = arcade.Sprite(arcade.resources.image_star)
stern.center_x = 100
stern.center_y = 200
sterne.append(stern)

# Nun können wir schauen ob das Alien einen Stern berührt
beruehrte_sterne = alien.collides_with_list(sterne)
for stern in beruehrte_sterne:
    # Die nächsten Befehle werden für jeden berührten Stern ausgeführt 
    # Man kann den Stern dann zum Beispiel entfernen
    stern.remove_from_sprite_lists()

```
