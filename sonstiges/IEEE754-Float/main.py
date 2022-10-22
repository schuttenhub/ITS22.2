#Eingabe Tastatur + Dezimalzahl mit Vorzeichenbit
def decimal_input():
    '''Input: Eingabe - Output: Tupel mit Float Dezimalzahl(0) + Vorzeichen(1) (- = 1, + = 0)'''
    decimal = float(input("Gib eine reelle Zahl ein: "))

    if str(decimal)[0] == "-":
        vorzeichen = 1
        return abs(decimal),vorzeichen
    else:
        vorzeichen = 0
        return decimal,vorzeichen

###### Variablen definieren
decimal_input_tuple = decimal_input()
decimal_str = str(decimal_input_tuple[0])
decimal_Ganz = int(decimal_str[:decimal_str.index(".")])
decimal_DecP = str(decimal_str[decimal_str.index(".")+1:])
vorzeichen = int(decimal_input_tuple[1])
ieee = int(0)
binary_Ganz = str()
binary_DecP = str()
before_norm = str()
after_norm = tuple()
character = str()
IEEE754var = str()

######Funktionen definieren
def Decimal_GanzInBinary(decimal_Ganz):
    '''Input dezimale Ganzzahl -> Output: binäre Ganzzahl'''
    binary_Ganz = str()
    if decimal_Ganz == 0:
        binary_Ganz = '0'
    while decimal_Ganz > 0:
        binary_Ganz += str(decimal_Ganz % 2)
        decimal_Ganz = decimal_Ganz // 2
    binary_Ganz = binary_Ganz[::-1]
    return binary_Ganz

def Decimal_DecPInBinary(decimal_DecP):
    '''Input: dezimale Nachkommastellen -> Output: binäre Nachkommastellen'''
    decimal_DecP = float(str("0.") + str(decimal_DecP))
    binary_DecP = str()
    while len(str(binary_DecP)) <= 42:
        if (decimal_DecP * 2) == 1.0:
            binary_DecP += "1"
            return binary_DecP
        if (decimal_DecP * 2) > 1.0:
            decimal_DecP = decimal_DecP * 2
            decimal_DecP -= 1
            binary_DecP += "1"
        if (decimal_DecP * 2) < 1.0:
            decimal_DecP = decimal_DecP * 2
            binary_DecP += "0"
    return binary_DecP

def normalize_binary(before_norm):
    '''Input: Binäre Float Zahl - Output: Tupel mit normalisierter fLoat Zahl(0) + Exponent(1)'''
    replace_dot = 1
    output_liste = list(before_norm)
    DotPosition = output_liste.index(".")
    if output_liste[0] == '1':
        output_liste.insert(1, output_liste.pop(output_liste.index(".")))
        return_value = ''.join(output_liste)
        return return_value,(DotPosition - replace_dot)
    else:
        replace_dot = output_liste.index('1')
        output_liste.insert(replace_dot, output_liste.pop(output_liste.index(".")))
        while True:
            output_liste.remove('0')
            if output_liste[0] == '1':
                return_value = ''.join(output_liste)
                return return_value,(DotPosition - replace_dot)
    
def Character(after_norm):
    '''input: Exponent -> Output: Character in Binärform'''
    character = int(after_norm[1]) + 127
    characterstr = str()
    while character > 0:
        characterstr += str(int(character % 2))
        character = character // 2
    characterstr = characterstr[::-1]
    while len(characterstr) < 8:
        characterstr = '0' + characterstr
    return characterstr

def IEEE754(vorzeichen,character,after_norm):
    '''Input: Alle anderen Ergebnisse -> Output: IEEE-754 konforme Binärzahl'''
    vorzeichen = str(vorzeichen)
    IEEEstr = str(vorzeichen)
    IEEEstr = IEEEstr + str(character)
    after_norm = str(after_norm[0])
    after_norm = str(after_norm[after_norm.index(".")+1:])
    IEEEstr = IEEEstr + after_norm
    return IEEEstr[:32]


###### Variablen mit Werten füttern
binary_Ganz = Decimal_GanzInBinary(decimal_Ganz)
binary_DecP = Decimal_DecPInBinary(decimal_DecP)
before_norm = "{}.{}".format(binary_Ganz,binary_DecP)
after_norm = normalize_binary(before_norm)
character = Character(after_norm)
IEEE754var = IEEE754(vorzeichen,character,after_norm)


###### Output der Ergebnisse
print("\n")
print(before_norm, "Float Darstellung")
print(after_norm[0], "Normalisierte Darstellung")
print("V<char--><----Mantisse--------->")
print(IEEE754var, "IEEE-754 Standard Darstellung")
print("\n")
