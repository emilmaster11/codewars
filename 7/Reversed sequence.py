###Mein code###
def reverse_seq(n):
    n = n
    ergebniss = []
    int = 0
    while int < n:
     ergebniss += [n-int]
     int += 1
    
    return ergebniss


###Besserer Code###
def reverseseq(n):
    return list(range(n, 0, -1))

print(reverse_seq(3))