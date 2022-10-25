#Wortgenerator
from operator import le
import string

def wort_generator():
    letters = string.ascii_lowercase
    word = 'aaaa'
    i_1 = ''
    i_2 = ''
    i_3 = ''
    i_4 = ''

    
    for i_1 in letters:
        word = i_1 + i_2 + i_3 + i_4
        if (wort_check_1(word) and wort_check_2(word)):
            print(word)

        for i_2 in letters:
            word = i_1 + i_2 + i_3 + i_4
            if (wort_check_1(word) and wort_check_2(word)):
                print(word)

            for i_3 in letters:
                word = i_1 + i_2 + i_3 + i_4
                if (wort_check_1(word) and wort_check_2(word)):
                    print(word)

                for i_4 in letters:
                    word = i_1 + i_2 + i_3 + i_4
                    if (wort_check_1(word) and wort_check_2(word)):
                        print(word)

                i_4 = letters[0]
            i_3 = letters[0]
        i_2 = letters[0]


def wort_check_1(word):
    konsonanten = 'bcdfghjklmnpqrstvwxyz'
    if len(word) <=3: #nur damit auch mindestens 4 Zeichen ausgegeben werden
        return False

    let_in_word = 0
    kons_count = 0
    for x in range(3):
        for i_check in konsonanten:
            if i_check == word[let_in_word]:
                let_in_word +=1
                kons_count +=1
                break
    if kons_count >= 3:
        return False
    else:
        return True

def wort_check_2(word):
    konsonanten = 'bcdfghjklmnpqrstvwxyz'
    let_in_word = 1
    kons_count = 0
    for x in range(3):
        for i_check in konsonanten:
            if i_check == word[let_in_word]:
                let_in_word += 1
                kons_count += 1
                break
    if kons_count >= 3:
        return False
    else:
        return True

wort_generator()