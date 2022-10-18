def bin_dec(bin_zahl):
    '''input: binary number, output: decimal number'''
    bin_zahl = str(bin_zahl)                                        #Zahl wird als String konvertiert
    bin_zahl = bin_zahl[::-1]                                       #Zahl wird umgedreht
    bin_list = list(bin_zahl)                             #Zahl wird einzeln in list geschrieben
    dec_zahl = int(0)
    i2 = 0
    for i in bin_list:
        if int(i) == 1:
            dec_zahl = dec_zahl + 2**i2
        i2 = i2 + 1
    return dec_zahl


def bin_oct(bin_zahl):
    '''input: binary number, output: octal number'''
    bin_zahl = str(bin_zahl)                                        #Zahl wird als String konvertiert
    bin_zahl = bin_zahl[::-1]                                       #Zahl wird umgedreht
    bin_list = list(bin_zahl[:3:])                             #Zahl wird einzeln in list geschrieben
    dec_zahl = int(0)
    i2 = 0
    for i in bin_list:
        if int(i) == 1:
            dec_zahl = dec_zahl + 2**i2
        i2 = i2 + 1
    return dec_zahl
