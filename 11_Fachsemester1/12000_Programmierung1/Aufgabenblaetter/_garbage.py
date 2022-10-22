#3.1 b)
from decimal import Decimal
from math import sqrt
nachkomma = 10
vergleiche_mit_pi = 15_000_000

def pi_calc(nachkomma, vergleiche_mit_pi):
    i = 1
    i2 = 0
    pi_vgl = Decimal(0)
    pi_org = Decimal(0)
    while True:
        pi_vgl = round(pi_org, nachkomma)
        pi_org = pi_org + Decimal(1) / Decimal(i**2)
        i += 1
        if pi_vgl == round(pi_org, nachkomma):
            i2 += 1
            if i2 == vergleiche_mit_pi:
                return Decimal(sqrt(pi_org * Decimal(6)))


print(pi_calc(nachkomma, vergleiche_mit_pi))
#Mehr als 6 oder 7 korrekte Nachkommastellen sind kaum in absehbarer Zeit möglich (+/- 30 Sekunden)