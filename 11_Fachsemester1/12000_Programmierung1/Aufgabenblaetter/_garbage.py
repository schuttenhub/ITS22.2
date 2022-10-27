d = {0:'Hallo', 'Hallo':2, 2:'Hallo', 3:4}

d_keys = list(d.keys())

print(type(d_keys[0]))

for i in range(len(d)):
    if d_keys[i] is type(int):
        print(f"Key {i}-{d_keys[i]} is type int")