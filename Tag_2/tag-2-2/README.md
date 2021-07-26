# Funktionen

Nehmen wir einmal das Baum-Beispiel 

```python
x = 290
y = 190

# Baumstamm
arcade.draw_xywh_rectangle_filled(x, y, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(x-20, y+30, x+10, y+110, x+40, y+30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(x,y, 3, arcade.color.RED)
```

Wenn ihr nun einen zweiten Baum malen wollt, müsst ihr nochmal alles neu schreiben.
Das ist vielleicht ein wenig umständlich. 
Viel besser wäre es doch, wenn ihr selbst eine Funktion schreiben könntet,
die einen Baum zeichnet...


```python
# Eine Funktion fängt an mit 'def', einem Namen und den Klammern
def baum(x, y): # In den Klammern könnt ihr angeben, welche informationen ihr braucht 
     # alle Befehle, die ausgeführt werden sollen, müssen eingerückt werden:
    arcade.draw_xywh_rectangle_filled(x, y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x-20, y+30, x+10, y+110, x+40, y+30, arcade.csscolor.DARK_GREEN)
    arcade.draw_circle_filled(x,y, 3, arcade.color.RED)
```

Wenn ihr nun einen Baum zeichnen wollte, geht das ganz einfach:

```python
baum(240, 190)
baum(290, 190)
```

> ✅ Aufgabe: Schreibt den neuen Code um, sodass Ihr Funktionen benutzen könnt.