#Aufgabe 3.3 c)
d = {0:'Hallo', 'Hallo':2, 2:'Hallo', 3:[4, 5, 6], }

d_keys = list(d.keys())
i = 0
while type(d_keys[i]) == int:
    d_keys_is_int = True
    i += 1

print(f"Alle Schlüssel sind int -> {d_keys_is_int}")