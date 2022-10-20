#i = 1
#zahl = 0.0
#zahlstr = str()
#ende = 250000     #206619
#
#
#while True:
#    zahl = zahl + 1/(i**3)
#    i += 1
#    zahlstr = str(zahl)
#
#    if i >= 40:
#        print(round(zahl, 10))
i = 1
zahl = 0.0
ende = 250000     #206619
zahl_vgl = 0
i2 = 0
while True:


    zahl = zahl + 1/(i**3)
    i += 1
    
    if round(zahl, 10) == zahl_vgl:
        i2 += 1
        if i2 == 10:
            print(round(zahl, 10))
    zahl_vgl = round(zahl, 10)