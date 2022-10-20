#Aufgabe 3.1
i = 1
zahl = 0.0
zahl_vgl = 0
i2 = 0
def zahl_komma(i, zahl, i2, zahl_vgl):
    while True:
        zahl = zahl + 1/(i**3)
        i += 1
        if round(zahl, 10) == zahl_vgl:
            i2 += 1
            if i2 == 300000:
                print((i-i2), "ausgeführte Iterationen.")
                print(i2, "verglichene Änderungen der Nachkommastellen bevor nicht mehr gerechnet wird.")
                return(round(zahl, 10))
        zahl_vgl = round(zahl, 10)

print(zahl_komma(i, zahl, i2, zahl_vgl),"lautet die Zahl.")

#zuerst habe ich die Schleife 250000 mal laufen lassen und dann die Funktion 206619 mal laufen lassen.
# Das war das Minimum für die letzte korrekte Nachkommastelle.
# Das Script war allerdings ineffizient und hat sehr langsam +10 Minuten.
# Die Zahl als genau genug gerundet auszugeben, wenn sich die Nachkommastelle i2-mal nicht mehr ändert
# geht deutlich schneller. So kann ich auch 1Mio Vergleiche innerhalb von wenigen Sekunden ausführen

