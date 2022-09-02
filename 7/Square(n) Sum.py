
def sum_array(a):
    input = a
    summe = 0
    schleife = 0 
    länge = len(input)

    while schleife < länge:
     summe += input[schleife]
     schleife += 1

    return summe

print(sum_array([1, 5.2, 4, 0, -1]))