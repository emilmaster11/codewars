def remove_char(s):
    string = s
    länge  = len(string)-1
    new_string = ""
    int = 0

    while int < länge:
     
     if int != 0 or int == länge:
         new_string += string[int]
     
     int += 1    
    
    return (new_string)


print(remove_char("Test"))

###'Was 1000 mal effektiver ist
def remove_char_fast(s):
    return s[1:len(s)-1]