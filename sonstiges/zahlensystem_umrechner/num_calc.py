def dec_bin(dez_zahl):
    '''get decimal number and return binary number'''
    bin_liste = []
    bin_zahl = 0

    while dez_zahl != 0:
        bin_liste.append(dez_zahl % 2)
        dez_zahl = dez_zahl // 2

    bin_zahl = ''.join(str(bin_zahl) for bin_zahl in bin_liste)     #-> Liste in String konvertieren
    bin_zahl = bin_zahl[::-1]                                       #string umdrehen
    return int(bin_zahl)                                            #string ausgeben

def dec_oct(dez_zahl):
    '''get decimal number and return oct number'''
    oct_liste = []
    oct_zahl = 0

    while dez_zahl != 0:
        oct_liste.append(dez_zahl % 8)
        dez_zahl = dez_zahl // 8

    oct_zahl = ''.join(str(oct_zahl) for oct_zahl in oct_liste)     #-> Liste in String konvertieren
    oct_zahl = oct_zahl[::-1]                                       #string umdrehen
    return int(oct_zahl)                                            #string ausgeben

def dec_hex(dez_zahl):
    '''get decimal number and return hex number'''
    hex_liste = []
    hex_zahl = 0

    while dez_zahl != 0:
        if dez_zahl % 16 >= 9:
            if dez_zahl % 16 == 10: hex_liste += ("A")
            if dez_zahl % 16 == 11: hex_liste += ("B")
            if dez_zahl % 16 == 12: hex_liste += ("C")
            if dez_zahl % 16 == 13: hex_liste += ("D")
            if dez_zahl % 16 == 14: hex_liste += ("E")
            if dez_zahl % 16 == 15: hex_liste += ("F")
        else:
            hex_liste.append(dez_zahl % 16)
        dez_zahl = dez_zahl // 16

    hex_zahl = ''.join(str(hex_zahl) for hex_zahl in hex_liste)     #-> Liste in String konvertieren
    hex_zahl = hex_zahl[::-1]                                       #string umdrehen
    return str(hex_zahl)