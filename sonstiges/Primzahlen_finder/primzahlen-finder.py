#Aufgabe 4.0 aber es werden Primzahlen bis zu einem eingegebenen Limit gerechnet
prim_calc_limit = int(input('Bitte Zahl eingeben '))


def prim(maybe_prim):
    prim_index = 0
    if maybe_prim == 0: return False
    if maybe_prim == 1: return False


    for i in range(maybe_prim):       
        rest = maybe_prim % (i+1)
        if rest == 0:
            prim_index += 1
        if prim_index > 2:
            return False
        if (maybe_prim > 20) and (i > ((maybe_prim//2) + 1) ): break

    
    return maybe_prim  

for i in range(prim_calc_limit):
    print_filter = prim(i)
    if type(print_filter) == int:
        print(print_filter)