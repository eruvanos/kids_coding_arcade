
# Denke wie ein Computer

Ein Beispiel: Robotkellner
1. Nimm das Essen auf
2. Gehe aus der Küche zum Tisch des Gastes
3. Setze das Essen ab


> ⚡️ Aber wie kommt der Roboter aus der Küche zum Gast?

1. Nimm das Essen auf
2. Gehe aus der Küche zum Tisch des Gastes 
    1. Gehe durch die Tür zwischen Küche und Gastraum
    2. Gehe von der Tür zum Gast
        1. Wenn ein Hindernis auf dem Weg ist: weiche aus
3. Setze das Essen ab

```python
robot = Robot()

robot.nehme_essen()
robot.gehe_zu("TÜR")
robot.gehe_zu("TISCH")
if robot.sieht_hindernis():
    robot.ausweichen()
robot.gebe_essen()
```

# Programmiersprachen

- **C** Oft benutzt für Betriebssysteme (Windows, Linux)
- **Java** Funktioniert auf Computern, Handys und Tablets.
- **JavaScript** Mit dieser Sprache werden oft Webseiten erstellt.
- **Scratch** Eine Bildersprache, die sich zum Lernen eignet.
- **Python** Eine Sprache, mit der man alle möglichen Dinge machen kann.

# Python
Überall auf der Welt und auch im Weltall benutzt. 
So wie die meisten Sprachen basiert sie auf Englisch. Das sind aber wirklich nur wenige Wörter.


## Befehle

Um dem Computer zu sagen was er machen soll, verwenden wir Befehle, sie werden auch Funktionen genannt.
Funktionen ruft man auf, in dem man ihren Namen schreibt und dann Klammern schreibt.
Wenn die Funktion noch Informationen benötigt, schreibt man diese zwischen die Klammern.

Die Funktion `print` kann dem Benutzer Text anzeigen:

```python
print()
print("Du wurdest gehacked!")
```

## Variable

Wenn der Computer sich Informationen merken soll,
kann man Variablen benutzen, Variablen haben einen Namen. 
Mit einem `=` speichert man die neuen Informationen, 
hier zum Beispiel unseren Text "Du wurdest gehacked!".

```python
text = "Du wurdest gehacked!"
print(text)
```

## Informationen

In Programmiersprachen gibt es verschiedene Arten von Informationen:
* Zahlen
* Buchstabenketten / Zeichenketten (Englisch: Strings)
* ...

```python
# Zahlen
1
1000

# Zeichenketten / Strings
"Hallo Welt!"
"100"
```









