def disemvowel(string_):
    list = ["a", "e", "i", "o", "u","A","E","I","O","U"]
    
    new_string = ""

    for a in string_:
     if a not in list:
        new_string += a

    return new_string

print(disemvowel("N ffns bt,\nr wrtng s mng th wrst 'v vr rd"))