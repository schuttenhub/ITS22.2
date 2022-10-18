from num_calc import dec_bin, dec_oct, dec_hex

print("Bitte gib eine (ganzzahlige) Zahl ein: \n")
dez_zahl = int(input())
print("In welches Zahlensystem soll umgerechnet werden? \n(O)ktal, (B)inär, (H)exadezimal?")
auswahl = str(input())

if auswahl == "O":
    print(dec_oct(dez_zahl))
if auswahl == "B":
    print(dec_bin(dez_zahl))
if auswahl == "H":
    print(dec_hex(dez_zahl))
