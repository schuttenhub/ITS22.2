from num_dec import dec_bin, dec_oct, dec_hex
from num_bin import bin_dec

print("Welches Zahlensystem soll umgerechnet werden? \n(D)ezimal, (B)inär, (O)ktal, (H)exadezimal?")
zahl = str(input())

print("In welches Zahlensystem soll umgerechnet werden? \n(D)ezimal, (B)inär, (O)ktal, (H)exadezimal?")
ziel_zahl = str(input())

if zahl == 'D':
    zahl = int(input('Bitte dezimale Zahl eingeben: '))
    if ziel_zahl == "O":
        print(dec_oct(zahl))
    if ziel_zahl == "B":
        print(dec_bin(zahl))
    if ziel_zahl == "H":
        print(dec_hex(zahl))

if zahl == 'B':
    zahl = int(input('Bitte binäre Zahl eingeben: '))
    if ziel_zahl == 'D':  
        print(bin_dec(zahl))
    if ziel_zahl == "O":
        print(dec_oct(zahl))
    if ziel_zahl == "B":
        print(dec_bin(zahl))
    if ziel_zahl == "H":
        print(dec_hex(zahl))