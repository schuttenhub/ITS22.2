#Umrechner von Dezimalzahlen in IEEE 754 Standard
from pickle import APPEND


decimal = abs(float(input("Gib eine Zahl ein (R): ")))
decimal_str = str(decimal)
decimal_Ganz = int(decimal_str[:decimal_str.index(".")])
decimal_DecP = int(decimal_str[decimal_str.index(".")+1:])



ieee = int(0)

def Decimal_GanzInBinary(decimal_Ganz):
    binarystr = str()
    while decimal_Ganz > 0:
        binarystr += str(int(decimal_Ganz % 2))
        decimal_Ganz = decimal_Ganz // 2
    binarystr = binarystr[::-1]
    return binarystr

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


def BinaryInIEEE(decimal, binary):
    #vorzeichen = 0
    #ieee = 0
    #ieeestr = ()
    #if decimal == 0:
    #    ieee = 00000000000000000000000000000000
    #    return ieee
    #if decimal > 0:
    #    vorzeichen = 0
    #else:
    #    vorzeichen = 1
    #
    #while True:
    pass
    #return ieee



binary_Ganz = Decimal_GanzInBinary(decimal_Ganz)
binary_DecP = Decimal_DecPInBinary(decimal_DecP)
print("{}.{}".format(binary_Ganz,binary_DecP))