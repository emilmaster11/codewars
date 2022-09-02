def xo(s):


 string = s
 int_O = 0
 int_X  = 0
 
 for a in string:
   if a == "x" or a == "X":
     int_X +=1
   
   if a == "o" or a == "O":
     int_O += 1

 if int_O == 0 and int_X == 0:
    return True
 
 if int_O == int_X:
    return True

 else:
    return False

 

#print(xo("zzoo"))



