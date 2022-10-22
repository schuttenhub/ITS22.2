#Umrechner von Dezimalzahlen in IEEE 754 Standard
def decimal_input():
    decimal = float(input("Gib eine reelle Zahl ein: "))

    if str(decimal)[0] == "-":
        vorzeichen = 1
        return abs(decimal)
    else:
        vorzeichen = 0
        return decimal,vorzeichen

decimal_input_tuple = decimal_input()
decimal_str = str(decimal_input_tuple[0])
decimal_Ganz = int(decimal_str[:decimal_str.index(".")])
decimal_DecP = int(decimal_str[decimal_str.index(".")+1:])
vorzeichen = int(decimal_input_tuple[1])

ieee = int(0)


binary_Ganz = str()
binary_DecP = str()
before_norm = str()

def Decimal_GanzInBinary(decimal_Ganz):
    binary_Ganz = str()
    while decimal_Ganz > 0:
        binary_Ganz += str(int(decimal_Ganz % 2))
        decimal_Ganz = decimal_Ganz // 2
    binary_Ganz = binary_Ganz[::-1]
    return binary_Ganz

def Decimal_DecPInBinary(decimal_DecP):
    decimal_DecP = float(str("0.") + str(decimal_DecP))
    binary_DecP = str()
    while len(str(binary_DecP)) <= 32:
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
    output_liste = list(before_norm)
    DotPosition = output_liste.index(".")
    output_liste.insert(1, output_liste.pop(output_liste.index(".")))
    return_value = ''.join(output_liste)
    return return_value,(DotPosition - 1)

def Character(before_IEEE):
    '''input Exponent'''
    character = int(before_IEEE[1]) + 127
    characterstr = str()
    while character > 0:
        characterstr += str(int(character % 2))
        character = character // 2
    characterstr = characterstr[::-1]
    return characterstr

    



binary_Ganz = Decimal_GanzInBinary(decimal_Ganz)
binary_DecP = Decimal_DecPInBinary(decimal_DecP)
before_norm = "{}.{}".format(binary_Ganz,binary_DecP)

before_IEEE = normalize_binary(before_norm)
print(before_IEEE)