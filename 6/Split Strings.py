def solution(s):
    
    line = s
    länge = len(line)
    
    n = 2
    string =  ([line[i:i+n] for i in range(0, len(line), n)])

    if int(länge) % 2 == 0:
     print(string)
     return string

    
    else:
     
     ausgabe = ''.join(string)
     ausgabe += '_'
     string =  ([ausgabe[i:i+n] for i in range(0, len(ausgabe), n)])
     print(string)
     
     return string


solution('abcdefg')
    



    
