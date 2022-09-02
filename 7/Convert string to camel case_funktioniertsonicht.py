from re import A, S
from unicodedata import decimal


def to_camel_case(text):
     neuer_buchstabe = ''
     
     umwandeln = ''
     
     lst = list(range(97 ,123))
     
     boolean_nächster_Buchstabe  = False

     for a in text:
        
        if boolean_nächster_Buchstabe:
            if a in lst:
                umwandeln = ord(a)
                umwandeln -= 32
                neuer_buchstabe +=chr(umwandeln)

            else:
                neuer_buchstabe += a
     
        boolean_nächster_Buchstabe = False    
        
        if a == '_' or a  == '-':
            boolean_nächster_Buchstabe = True

        else:
         neuer_buchstabe += a  
    
     return neuer_buchstabe      


print (to_camel_case('A_c-C'))


